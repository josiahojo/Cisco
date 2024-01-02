# README

This script is used to verify if the licence authorization (Enterprise to MPP) successfully applied to a group of Cisco IP Phone's after the firmware update.  The "Transition Authorization Status" is webscraped from the IP Phone's web server after the firmware update has been completed and the information is output to a log file.

Example Logs:

--------------  192.168.1.1  --------------- 
#<td class="info" colspan="3">[0][01/01/2023 12:00:00][https://cloudupgrader.webex.com/licenses/e2m/00B0D063C226.lic]Authorization Succeeded.</td>
#<td class="info" colspan="3"></td>
--------------   END    -------------------- 

Transition Authorization Status (information where the logs are scraped)

![image](https://github.com/sound-selection/ip-phones/assets/95934365/6c847097-c618-403b-a071-1c0fc086c82b)
