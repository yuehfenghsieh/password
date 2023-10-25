password = 123456789
i = 3 
while i > 0:
	i = i - 1
	pwd = input('請輸入密碼')
	if pwd == password:
		print('登入成功')
		break
	else:
		if i > 0:
			print('密碼輸入錯誤，還有', i, '次機會')
		else:
			print('帳號封鎖')