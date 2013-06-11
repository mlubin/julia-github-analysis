# https://github.com/jacquev6/PyGithub
from github import Github

g = Github("user","pass")

juliarepo = g.get_user("JuliaLang").get_repo("julia")

openissues = juliarepo.get_issues(sort="created",direction="asc",state="open")
closedissues = juliarepo.get_issues(sort="created",direction="asc",state="closed")
fd = open("issuedata.wsv",'w')
print >>fd,"ID","User","Date","Status"

for issue in openissues:
	print >>fd,issue.number,issue.user.login,issue.created_at.date(), issue.state
for issue in closedissues:
	print >>fd,issue.number,issue.user.login,issue.created_at.date(), issue.state
fd.close()
