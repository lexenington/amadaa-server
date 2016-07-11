print("checking if schema versioning is installed")
import amadaa.schema
amadaa.schema.setup()

print("check if role is installed")
import amadaa.role.schema

print("checking if user is installed")
import amadaa.user.schema
