
'''
This changes 404 and 403 errors to NULL to filled out by me.

UPDATE ChatbotWebsiteOrganizer

SET website_name = NULL

WHERE website_name LIKE '%404%' OR website_name LIKE '%403%'
'''
'''
This changes plain Youtube video titles to NULL to be filled out by me.

UPDATE ChatbotWebsiteOrganizer

SET website_name = NULL

WHERE website_name = 'YouTube'
'''
'''
SELECT Topic, URL, Website_Name, Joining_Date

FROM ChatbotWebsiteOrganizer

ORDER BY Topic ASC
'''