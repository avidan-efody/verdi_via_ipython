import os
import subprocess
import uuid
import re

class verdi:
    def __init__(self, design_dir, fsdb_location):
        self.verdi_uid = str(uuid.uuid4())
        self.design_dir = design_dir
        self.fsdb_location = fsdb_location
        subprocess.Popen(["verdi","-tkName", self.verdi_uid, "-dbdir", design_dir, "-ssf", fsdb_location]) 

    def _wish(self, args):
        print(args)
        result = subprocess.run(["wish", "send_to_verdi.tcl", self.verdi_uid] + args, stdout=subprocess.PIPE)
        return result.stdout

    def find_signals(self, hier_root, pattern, max_depth=100):
        onesearch_output = os.popen(os.environ['VERDI_HOME'] + '/bin/onesearch ' + ' --rootdir ' + self.design_dir + 
        	' --plain ' + ' -- ' + ' "' + pattern + '" ' + ' "scopes:' + hier_root + '" ' + ' "' + "Identifiers:" + '" ').read()

        result = []

        for signal_match in re.finditer('(?<=scope: ).*', onesearch_output):
            signal_name = signal_match.group(0)
            if (signal_name.count(".") <= max_depth):

            	result = result + [signal_name.replace(".","/")]

        return result




