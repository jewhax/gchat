import gnupg
from conf import settings

class GPG():
    def __init__(self, fingerprint='', passphrase=''):
        self.fingerprint = ''
        self.passphrase = ''

    def setPassphrase(self, passphrase): self.passphrase = passphrase
    def getPassphrase(self): return self.passphrase
    def setFingerprint(self, fingerprint): self.fingerprint = fingerprint
    def getFingerprint(self): return self.fingerprint


def main():
    gpg = GPG()

if __name__ == '__main__':
    main()