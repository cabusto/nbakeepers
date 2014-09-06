from app import ma

class RotoEvilStatMarshal(ma.Serializer):
    class Meta:
        fields = ('id', 'rank', 'name', 'yahoo', 'auction', 'PPG', 'RPG', 'APG', 'THREEPM', 'SPG','BPG','FGPCT','FTPCT')
