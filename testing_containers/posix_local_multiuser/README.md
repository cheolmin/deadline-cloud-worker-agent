
This is a docker container that is intended to be used to set up a Linux environment within which we can
test the ability of the Worker Agent to run Jobs as a different user than the agent is running as.

Users are set up as local accounts. The worker agent overrides the queue's jobRunAsUser with
the local "jobuser" user.
