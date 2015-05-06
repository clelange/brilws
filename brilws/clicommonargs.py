from brilws import api,params
import re,time
from datetime import datetime

class parser(object):
    def __init__(self,argdict):
        self._argdict = argdict
        self._dbconnect = None 
        self._authpath = None
        self._beamstatus = None
        self._egev = None
        self._datatagname = None
        self._amodetag = None
        self._fillmin = None
        self._fillmax = None
        self._runmin = None
        self._runmax = None
        self._tssecmin = None
        self._tssecmax = None
        self._runlsSeries = None
        self._withBX = False
        self._chunksize = None
        self._ofilename = '-'
        self._fh = None
        self._totable = False
        self._outputstyle = 'tab'
        self._parse()
        
    def _parse(self):
        self._dbconnect = self._argdict['-c']
        self._authpath = self._argdict['-p']
        if self._argdict['--beamstatus']: self._beamstatus = self._argdict['--beamstatus'].upper()
        self._egev = self._argdict['--beamegev']
        self._datatagname = self._argdict['--datatag']
        self._amodetag = self._argdict['--amodetag']
        self._chunksize = self._argdict['--chunk-size']
        self._outputstyle = self._argdict['--output-style']
        if self._argdict['--xing']:
            self._withBX = True
        if self._argdict['-f'] :
            self._fillmin = self._argdict['-f']
            self._fillmax = self._argdict['-f']
        if self._argdict['-i']: # -i has precedance over -r
            fileorpath = self._argdict['-i']
            self._runlsSeries = api.parsecmsselectJSON(fileorpath)
        elif self._argdict['-r'] :
            self._runmin = self._argdict['-r']
            self._runmax = self._argdict['-r']
        s_beg = None
        s_end = None
        if not self._argdict['-f'] and not self._argdict['-r']:
            if self._argdict['--begin']:
                s_beg = self._argdict['--begin']
                for style,pattern in {'fill':params._fillnum_pattern,'run':params._runnum_pattern, 'time':params._time_pattern}.items():
                    if re.match(pattern,s_beg):
                        self._fillmin = int(s_beg)
                    elif style=='run':
                        self._runmin = int(s_beg)
                    elif style=='time':
                        self._tssecmin = int(time.mktime(datetime.strptime(s_beg,params._datetimefm).timetuple()))
            if self._argdict['--end']:
                s_end = self._argdict['--end']
                for style,pattern in {'fill':params._fillnum_pattern,'run':params._runnum_pattern, 'time':params._time_pattern}.items():
                      if re.match(pattern,s_end):
                          if style=='fill':
                              self._fillmax = int(s_end)
                          elif style=='run':
                              self._runmax = int(s_end)
                          elif style=='time':
                              self._tssecmax = int(time.mktime(datetime.strptime(s_end,params._datetimefm).timetuple()))
        
        if self._argdict['-o'] or self._outputstyle == 'csv':
            if self._argdict['-o']:
                self._outputstyle = 'csv'                
                self._ofilename = self._argdict['-o']
                self._fh = open(self._ofilename,'w')                
            else:
                self._fh = sys.stdout
        else:
            self._totable = True
            
    @property
    def dbconnect(self):
        return self._dbconnect
    @property
    def authpath(self):
        return self._authpath
    @property
    def beamstatus(self):
        return self._beamstatus
    @property
    def egev(self):
        return self._egev
    @property
    def datatagname(self):
        return self._datatagname
    @property
    def amodetag(self):
        return self._amodetag
    @property
    def fillmin(self):
        return self._fillmin
    @property
    def fillmax(self):
        return self._fillmax
    @property
    def runmin(self):
        return self._runmin
    @property
    def runmax(self):
        return self._runmax
    @property
    def tssecmin(self):
        return self._tssecmin
    @property
    def tssecmax(self):
        return self._tssecmax
    @property
    def runlsSeries(self):
        return self._runlsSeries
    @property
    def withBX(self):
        return self._withBX
    @property
    def chunksize(self):
        return self._chunksize
    @property
    def ofilehandle(self):
        return self._fh
    @property
    def outputstyle(self):
        return self._outputstyle
    @property
    def totable(self):
        return self._totable    
    
class validator(object):
    def __init__(self):
        pass
    