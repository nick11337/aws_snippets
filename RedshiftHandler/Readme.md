<h1>Redshift Handler (can be used as a lambda layer)</h1>

Package to work with a redshift in AWS. Can be modified to use with another database.

<hr>

**How to use:**

1. Import dependencies
```py
from redshift_utils import Messages, ScriptReader, RedshiftDataManager
from settings import SCRIPT_PATH
```
2. Set script path in settings.sql
```
###############################################
# Script settings and constants.
###############################################
SCRIPT_PATH = 'script.sql'  # ToDo set to path

```
3. Set up DB_CONNECTION
```
DB_CONNECTION = {
    'db_host': get_config(Vars.REDSHIFT_HOST),
    'db_name': get_config(Vars.REDSHIFT_DB_NAME),
    'db_username': get_config(Vars.REDSHIFT_USERNAME),
    'db_password': os.getenv("REDSHIFT_PASSWORD")
}
```
4. Define the script in the script.sql
```sql
SELECT * from {0} where kundennummer == {1}
```
5. Get the script with ```get_script``` and fill in all parameters you want. 

```py
script = ScriptReader.get_script(SCRIPT_PATH).format(kundennummer)
```
6. Run the query and get the results (if possible)
```py
result = RedshiftDataManager.run_query(script, DB_CONNECTION)
```