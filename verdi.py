import subprocess
import uuid

class verdi:
    def __init__(self, design_dir, fsdb_location):
        self.verdi_uid = str(uuid.uuid4())
        subprocess.Popen(["verdi","-tkName", self.verdi_uid, "-dbdir", design_dir, "-ssf", fsdb_location]) 

    def wish(self, args):
        print(args)
        result = subprocess.run(["wish", "send_to_verdi.tcl", self.verdi_uid] + args, stdout=subprocess.PIPE)
        return result.stdout
