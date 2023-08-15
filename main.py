from sources.other_sources.run_with_elevated_rights.run_as_admin import RunAsAdmin
from sources.other_sources.run_with_elevated_rights.run_as_trusted_installer import RunAsTrustedInstaller
import sys


if __name__ == "__main__":
    run_as_admin = RunAsAdmin()
    run_as_trustedinstaller = RunAsTrustedInstaller()

    if not run_as_admin.run_as_admin():
        sys.exit(1)

    run_as_trustedinstaller.run_as_trustedinstaller()
