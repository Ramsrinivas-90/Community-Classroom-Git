from dotenv import dotenv_values
config = dotenv_values("../.env")
PYRODBUserName = config['PYROUSERNAME']
PYRODBPassword = config['PYROPASSWORD']
BVDBUserName = config['BVUSERNAME']
BVDBPassword = config['BVPASSWORD']
