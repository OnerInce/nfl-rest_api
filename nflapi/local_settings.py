DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dcfuj0v6fk4c6g',
        'USER': 'wesocouvmtvlmv',
        'PASSWORD': 'c2587d078b6d5254de4445f742ee40d29f6f7ece0d10dd4d6929752cf394442d',
        'HOST': 'ec2-52-0-65-165.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}

import dj_database_url
db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)


#################################################################
    ##  (CORS) Cross-Origin Resource Sharing Settings ##
#################################################################
CORS_ORIGIN_ALLOW_ALL = True