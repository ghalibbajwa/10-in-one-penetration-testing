
from apps.home.libs.CMSeeK.cmseekdb import basic as cmseek
from apps.home.libs.CMSeeK.cmseekdb import core as core

def run_test(test):
    cmseek.redirect_conf = '1'
    cua = None
    s =test['test_url']
    target = cmseek.process_url(s)
    if target != '0':
        if cua == None:
            cua = cmseek.randomua()
        core.main_proc(target,cua,test['id'])
        cmseek.handle_quit()

