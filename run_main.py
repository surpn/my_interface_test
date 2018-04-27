from common.runner import TestRunner
from common.sendemail import sendemail
from common.utils import newest_file

run = TestRunner(title="iccard_test", description="test")
run.run()
mail_file = newest_file("result/report")
print(mail_file)
sendemail(subject="iccard_test", context="test", mail_file=mail_file)
