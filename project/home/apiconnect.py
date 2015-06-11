from rauth import OAuth1Service
from rauth.utils import parse_utf8_qsl
import pickle
import time

class apiConnect:
    # access token lifetime in seconds
    access_token_lifetime = 3600

    # one request every X seconds to try to prevent 999 error codes
    request_period = 2   
    
    authorize_url = ""
    request_token = ""
    request_token_secret = ""
    saved_token = None
    oauth = None
    
    def __init__(self, keyfile, tokenfile=None):

        self.saved_token = None

        # read in consumer key and consumer secret key from file
        f = open(keyfile, "r")
        keys = f.read().split()
        f.close()

        if len(keys) != 2:
            raise RuntimeError('Incorrect number of keys found in ' + keyfile)

        consumer_key, consumer_secret = keys

        self.oauth = OAuth1Service(
            consumer_key = consumer_key,
            consumer_secret = consumer_secret,
            name = "yahoo",
            request_token_url = "https://api.login.yahoo.com/oauth/v2/get_request_token",
            access_token_url = "https://api.login.yahoo.com/oauth/v2/get_token",
            authorize_url = "https://api.login.yahoo.com/oauth/v2/request_auth",
            base_url = "http://fantasysports.yahooapis.com/")

        self.last_request = time.time()

        if tokenfile is not None:
            try:
                f = open(tokenfile, "r")
                self.saved_token = pickle.load(f)
                f.close()
            except IOError:
                self.saved_token = None

        if (self.saved_token is not None and
                self.saved_token["access_token"] and
                self.saved_token["access_token_secret"] and
                self.saved_token["session_handle"]):

            # refresh access token, it may not have expired yet but refresh
            # anyway
            self.refresh_access_token()

        else:
            self.request_token, self.request_token_secret = \
                self.oauth.get_request_token(params={"oauth_callback": "oob"})

            self.authorize_url = self.oauth.get_authorize_url(self.request_token)
            
            print self.authorize_url
            
    def connect(self, access_code):
        self.access_token_time = time.time()
        verification_code = access_code
        
        print verification_code
        
        raw_access = self.oauth.get_raw_access_token(
            self.request_token, self.request_token_secret,
            params={"oauth_verifier": verification_code})
        
        print "raw_access" 
        print raw_access.content

        parsed_access_token = parse_utf8_qsl(raw_access.content)
 
        self.saved_token = {}
        self.saved_token["access_token"] = parsed_access_token["oauth_token"]
        self.saved_token["access_token_secret"] = \
        parsed_access_token["oauth_token_secret"]
        self.saved_token["session_handle"] = \
        parsed_access_token["oauth_session_handle"]

        if tokenfile is not None:
            try:
                f = open(tokenfile, "w")
                pickle.dump(self.saved_token, f)
                f.close()
            except IOError:
                pass

            self.session = self.oauth.get_session(
                (self.saved_token["access_token"],
                 self.saved_token["access_token_secret"]))

    def refresh_access_token(self):
        self.access_token_time = time.time()

        (access_token, access_token_secret) = \
                    self.oauth.get_access_token(
                            self.saved_token["access_token"],
                            self.saved_token["access_token_secret"],
                            params={"oauth_session_handle":
                                    self.saved_token["session_handle"]})

        self.session = self.oauth.get_session(
                    (access_token, access_token_secret))

    def request(self, request_str):
        now = time.time()
        tdiff = max(0, now - self.last_request)
        self.last_request = now
        if tdiff > 0 and tdiff < self.request_period:
            time.sleep(tdiff)

        # check if our access token has expired
        now = time.time()
        tdiff = max(0, now - self.access_token_time)

        # refresh 60 seconds before it expires
        if tdiff > self.access_token_lifetime - 60:
            self.refresh_access_token()

        return self.session.get(request_str)
    
    def getURL(self):
        return str(self.authorize_url)
    

