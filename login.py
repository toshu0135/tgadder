o
    ÞØÎb"  ã                   @   s
  d dl mZmZ d dlmZmZmZmZmZm	Z	m
Z
 d dlmZmZ d dl mZ d dlmZ d dlmZmZ d dlZd dlZd dlZd dlZe  ejZejZejZejZejZ ej!Z"ej#Z$ej%Z&eeee e"e&e$gZ'dd	 Z(d
Z)dZ*e(  e+e de Z,zede, e)e*dZ-W n e.y£ Z/ ze0e1e/  W Y dZ/[/ndZ/[/ww ze- 2¡  W n e3y»   e- 4¡  e- 2¡  Y nw ze- 5e,¡Z6W n9 eyß Z/ ze0e e/ e  W Y dZ/[/n"dZ/[/w eyë   e0d Y n e	yü   e0e de  Y nw ze+e de Z7W n e8y   e0e d Y nw e7Z9ze-j:e,e6j;d <e1e9¡d W n ey=   e0e d Y n~ eyM   e0e d Y nn e
y   z	e+e$ dZ=W n e8yn   e0e d Y nw e=Z>ze- ?e>¡ W n  e.y Z/ ze0e de$ e1e/  W Y dZ/[/ndZ/[/ww Y n  e.yº Z/ ze0e de" e1e/  W Y dZ/[/ndZ/[/ww e0e$ e- @¡ jA de  de d e0e$ d e- 4¡  e+e  de de  de d ZBeBd!krôe Cd"¡ dS eBd#krÿe0d$ dS e0d% dS )&é    )ÚClientÚfilters)Ú	FloodWaitÚApiIdInvalidÚPhoneCodeExpiredÚPhoneCodeInvalidÚUserNotParticipantÚPhoneNumberInvalidÚSessionPasswordNeeded)ÚPeerIdInvalidÚChatAdminRequired)Úerrors)Ú	Forbidden)ÚinitÚForeNc                  C   s<   dd l } g d¢}|D ]}t|  t¡ |  q
td d S )Nr   )uu   âââââââ ââââââââ ââââââ âââââââââââââââââu{   âââââââââââââââââââââââââââââââââââââââââuh   ââââââââââââââ  ââââââââââââââââ   âââuh   ââââââââââââââ  ââââââââââââââââ   âââuh   âââââââââââââââââââ  âââââââââââ   âââuf   âââââââ âââââââââââ  âââââââââââ   âââz+=============Dev-@Godmrunal==============

)ÚrandomÚprintÚchoiceÚcolors)r   ÚbÚchar© r   ú%/storage/emulated/0/pyrogram/login.pyÚbanner#   s
   
r   i<|z Z 9b70b20efd67e9b99edc395d78407cfazSend Your Phone Numberzmemory/)Úapi_idÚapi_hashzsed api invalidz%The Provided Phone Number is invalid.zenter otp ypu recivedzTimeout.ú )Z
phone_codezInvalid OtpzThe otp has been expiredzSend 2FA Passwordz* Sorry You have reached limit of 5 Minuteszerror :z: z----> Signed Up Sucess

z$Session Sucesfully Saved in :memory:zpress zY z,if you want login another Number Else Press z N

ÚYzpython login.pyÚNZDonezplease choose options)DZpyrogramr   r   Zpyrogram.errorsr   r   r   r   r   r	   r
   Z*pyrogram.errors.exceptions.bad_request_400r   r   r   r   Zcoloramar   r   ÚtimeÚsysZrequestsÚosZRESETÚnZLIGHTGREEN_EXZlgZLIGHTRED_EXÚrZWHITEÚwZCYANÚcyZLIGHTYELLOW_EXZyeZLIGHTMAGENTA_EXZmgZLIGHTBLUE_EXZlbr   r   r   r   ÚinputZphone_numberZsessionÚ	ExceptionÚer   ÚstrZconnectÚConnectionErrorZ
disconnectZ	send_codeÚcodeZotpÚTimeoutErrorZotp_codeZsign_inZphone_code_hashÚjoinZtwo_step_codeZnew_codeZcheck_passwordZget_meZ
first_nameZsedÚsystemr   r   r   r   Ú<module>   s¬    $	ÿþ ÿÿ ÿ&ÿ&ÿ$ 

