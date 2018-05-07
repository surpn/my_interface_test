import smtplib
from email.header import Header
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP

import os

from common.readConfig import Config
from common.utils import current_path
from common.log import Log


def sendemail(subject="", context="", image=None, mail_file=None):
	"""
	发送邮件
	:param subject:邮件主题
	:param context: 邮件正文
	:param image: 邮件图片
	:param mail_file: 邮件附件
	:return:
	"""
	__config = Config().email()
	# 获取配置信息
	smtp_server = __config["smtp_server"]
	user = __config["user"]
	password = __config["password"]
	sender = __config["sender"]
	receiver = __config["receiver"]
	__log = Log().log()
	msg = MIMEMultipart('related')
	# 主题.收发人
	msg['Subject'] = Header(subject, 'utf-8')
	msg['From'] = sender
	msg['To'] = receiver

	# 正文
	msg.attach(MIMEText(context, 'plain', 'utf-8'))

	# 添加图片
	if image is not None:
		msgAlternative = MIMEMultipart('alternative')
		msg.attach(msgAlternative)

		mail_msg = '<img src="cid:image1"><br>'
		msgAlternative.attach(MIMEText(mail_msg, 'html', 'utf-8'))

		# 指定图片为当前目录
		with open(image, 'rb') as ff:
			msgimage = MIMEImage(ff.read())

		# 定义图片 ID，在 HTML 文本中引用
		msgimage.add_header('Content-ID', '<image1>')
		msg.attach(msgimage)

	# 附件
	if mail_file is not None and os.path.exists(mail_file):
		msg_file = MIMEText(open(mail_file, 'rb').read(), 'base64', 'utf-8')
		msg_file['Content-Type'] = 'application/octet-stream'
		msg_file['Content-Disposition'] = 'attachment; filename=test_report.html'
		msg.attach(msg_file)

	try:
		# 发送
		smtp = SMTP()
		# 1.连接邮件服务器
		smtp.connect(smtp_server)
		# 2.登录
		smtp.login(user, password)
		# 3.发送邮件
		smtp.sendmail(sender, receiver, msg.as_string())
		# 4.退出
		smtp.quit()
		__log.info("send email sessful")
	except Exception as e:
		__log.error(e)


if __name__ == "__main__":
	f = current_path() + '/test_case_data/test.png'
	sendemail("邮件主题", "邮件正文")
