PROPERTY RENTAL MANAGEMENT SYSTEM - GUI PACKAGE

Files included:
  main.py
  GUI/__init__.py
  GUI/gui_helpers.py
  GUI/login_gui.py
  GUI/admin_dashboard.py
  GUI/owner_dashboard.py
  GUI/tenant_dashboard.py
  GUI/property_gui.py
  GUI/owner_gui.py
  GUI/tenant_gui.py
  GUI/rent_gui.py
  GUI/complaint_gui.py

Installation:
1. Back up your existing GUI folder and main.py.
2. Copy the GUI folder and main.py from this package into your project root.
3. Keep your existing DAO, MODEL, Database, and Controller folders.
4. Run main.py from the project root, not from inside GUI.

Important integration note:
The GUIs call the controller methods shared earlier in this conversation. Existing database schema/status values and DAO result shapes must match those files. This package has not been run against your local database, so perform the agreed full test round after the files are installed. Never overwrite your existing project without keeping a backup.
