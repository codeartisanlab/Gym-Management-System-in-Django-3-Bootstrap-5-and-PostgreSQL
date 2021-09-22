from django import template
from main.models import Subscription,SubPlan
from django.contrib.auth.models import User
from datetime import date

register=template.Library()

@register.simple_tag
def check_user_package(user_id,plan_id):
	user=User.objects.get(id=user_id)
	plan=SubPlan.objects.get(id=plan_id)
	check_package=Subscription.objects.filter(user=user,plan=plan).count()
	if check_package > 0:
		return True
	else:
		return False

@register.simple_tag
def check_pckg_validity(user_id,plan_id):
	expired=False
	pdays=None
	pvalidity=None
	user=User.objects.get(id=user_id)
	plan=SubPlan.objects.get(id=plan_id)
	check_package=Subscription.objects.filter(user=user,plan=plan).count()
	if check_package > 0:
		pdata=Subscription.objects.filter(user=user,plan=plan).order_by('-id').first()
		today=date.today()
		pdate=pdata.reg_date
		pdays=(today-pdate).days
		pvalidity=pdata.plan.validity_days
		if pdays > pvalidity:
			expired=True
	else:
		expired=False
	return expired

	