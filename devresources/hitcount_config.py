"""
This is the number of days, weeks, months, 
hours, etc (using a timedelta keyword argument), 
that an Hit is kept active. 
If a Hit is active a repeat viewing will not be counted. 
After the active period ends, however, a new Hit will be recorded. 
You can decide how long you want this period to last 
and it is probably a matter of preference
"""
HITCOUNT_KEEP_HIT_ACTIVE = { 'days': 2 }


"""
Limit the number of active Hits from a single IP address. 
0 means that it is unlimited.
"""
HITCOUNT_HITS_PER_IP_LIMIT = 0


"""
Exclude Hits from all users in the specified user groups. 
By default, this is set to an empty list (all users counted). 
In the example, below, it will exclude all your ‘Editors’.
"""
# HITCOUNT_EXCLUDE_USER_GROUP = ( 'Editor', )


"""
Hits remain in the database indefinitely unless you run the 
hitcount_cleanup management command. 
This setting specifies a timedelta within which to keep/save Hits. 
Any Hit older than the time specified will be removed from the Hits table.
"""
HITCOUNT_KEEP_HIT_IN_DATABASE = { 'days': 365 }
