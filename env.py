from dotenv import dotenv_values
config = dotenv_values(".env")
PYRODBUserName = config['PYROUSERNAME']
PYRODBPassword = config['PYROPASSWORD']
PYRODBPORT = config['PYROPORT']
BVDBUserName = config['BVUSERNAME']
BVDBPassword = config['BVPASSWORD']
BVDBPORT = config['BVPORT']
BBDBUserName = config['BBUSERNAME']
BBDBPassword = config['BBPASSWORD']
BBDBPORT = config['BBPORT']
