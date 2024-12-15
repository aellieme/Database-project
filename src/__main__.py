import os
import sys
from Application import Application
from MainWindow import MainWindow

import psycopg2
import settings as st


def createdb():
    os.system('./createdb_script.sh')


def main():
    try:
        psycopg2.connect(**st.db_params)
        print(f'''Database "{st.db_params['dbname']}" exists''', file=sys.stderr)
    except psycopg2.OperationalError:
        createdb()
        print(f'''Created database "{st.db_params['dbname']}"''', file=sys.stderr)
    
    app = Application(sys.argv)

    main_window = MainWindow()
    main_window.showMaximized()

    result = app.exec()
    sys.exit(result)


if __name__ == '__main__':
    main()
