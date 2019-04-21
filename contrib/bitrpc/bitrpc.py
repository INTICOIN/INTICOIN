from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
#from jsonrpc import ServiceProxy, authProxy
import sys
import string

# ===== BEGIN USER SETTINGS =====
# if you do not set these you will be prompted for a password for every command
rpcuser = "qollqrex2"
rpcpass = "x"
# ====== END USER SETTINGS ======

# rpc_user and rpc_password are set in the bitcoin.conf file

#if rpcpass == "x":
	#rpc_connection = AuthServiceProxy("http://%s:%s@127.0.0.1:55884")
	#rpc_connection = ServiceProxy("http://127.0.0.1:55884")
#else:
rpc_connection = AuthServiceProxy("http://%s:%s@127.0.0.1:55884"%(rpcuser, rpcpass))
	#rpc_connection = AuthServiceProxy("http://%s:%s@127.0.0.1:55884"%(rpcuser, rpcpass))
	#rpc_connection = ServiceProxy("http://"+rpcuser+":"+rpcpass+"@127.0.0.1:55884")
#best_block_hash = rpc_connection.getbestblockhash()
#print(rpc_connection.getblock(best_block_hash))


cmd = sys.argv[1].lower()

if cmd == "backupwallet":
	try:
		path = raw_input("Enter destination path/filename: ")
		print rpc_connection.backupwallet(path)
	except:
		print "\n---An error occurred---\n"

elif cmd == "getaccount":
	try:
		addr = raw_input("Enter a Bitcoin address: ")
		print rpc_connection.getaccount(addr)
	except:
		print "\n---An error occurred---\n"

elif cmd == "getaccountaddress":
	try:
		acct = raw_input("Enter an account name: ")
		print rpc_connection.getaccountaddress(acct)
	except:
		print "\n---An error occurred---\n"

elif cmd == "getaddressesbyaccount":
	try:
		acct = raw_input("Enter an account name: ")
		print rpc_connection.getaddressesbyaccount(acct)
	except:
		print "\n---An error occurred---\n"

elif cmd == "getbalance":
	try:
		acct = raw_input("Enter an account (optional): ")
		mc = raw_input("Minimum confirmations (optional): ")
		try:
			print rpc_connection.getbalance(acct, mc)
		except:
			print rpc_connection.getbalance()
	except:
		print "\n---An error occurred---\n"

elif cmd == "getblockbycount":
	try:
		height = raw_input("Height: ")
		print rpc_connection.getblockbycount(height)
	except:
		print "\n---An error occurred---\n"

elif cmd == "getblockcount":
	try:
		print rpc_connection.getblockcount()
	except:
		print "\n---An error occurred---\n"

elif cmd == "getblocknumber":
	try:
		print rpc_connection.getblocknumber()
	except:
		print "\n---An error occurred---\n"

elif cmd == "getconnectioncount":
	try:
		print rpc_connection.getconnectioncount()
	except:
		print "\n---An error occurred---\n"

elif cmd == "getdifficulty":
	try:
		print rpc_connection.getdifficulty()
	except:
		print "\n---An error occurred---\n"

elif cmd == "getgenerate":
	try:
		print rpc_connection.getgenerate()
	except:
		print "\n---An error occurred---\n"

elif cmd == "gethashespersec":
	try:
		print rpc_connection.gethashespersec()
	except:
		print "\n---An error occurred---\n"

elif cmd == "getinfo":
	try:
		print(rpc_connection.getinfo())
	except:
		print "\n---An error occurred---\n"

elif cmd == "getnewaddress":
	try:
		acct = raw_input("Enter an account name: ")
		try:
			print(rpc_connection.getnewaddress(acct))
		except:
			print(rpc_connection.getnewaddress())
	except:
		print "\n---An error occurred---\n"

elif cmd == "getreceivedbyaccount":
	try:
		acct = raw_input("Enter an account (optional): ")
		mc = raw_input("Minimum confirmations (optional): ")
		try:
			print rpc_connection.getreceivedbyaccount(acct, mc)
		except:
			print rpc_connection.getreceivedbyaccount()
	except:
		print "\n---An error occurred---\n"

elif cmd == "getreceivedbyaddress":
	try:
		addr = raw_input("Enter a Bitcoin address (optional): ")
		mc = raw_input("Minimum confirmations (optional): ")
		try:
			print rpc_connection.getreceivedbyaddress(addr, mc)
		except:
			print rpc_connection.getreceivedbyaddress()
	except:
		print "\n---An error occurred---\n"

elif cmd == "gettransaction":
	try:
		txid = raw_input("Enter a transaction ID: ")
		print rpc_connection.gettransaction(txid)
	except:
		print "\n---An error occurred---\n"

elif cmd == "getwork":
	try:
		data = raw_input("Data (optional): ")
		try:
			print rpc_connection.gettransaction(data)
		except:
			print rpc_connection.gettransaction()
	except:
		print "\n---An error occurred---\n"

elif cmd == "help":
	try:
		cmd = raw_input("Command (optional): ")
		try:
			print rpc_connection.help(cmd)
		except:
			print rpc_connection.help()
	except:
		print "\n---An error occurred---\n"

elif cmd == "listaccounts":
	try:
		mc = raw_input("Minimum confirmations (optional): ")
		try:
			print rpc_connection.listaccounts(mc)
		except:
			print rpc_connection.listaccounts()
	except:
		print "\n---An error occurred---\n"

elif cmd == "listreceivedbyaccount":
	try:
		mc = raw_input("Minimum confirmations (optional): ")
		incemp = raw_input("Include empty? (true/false, optional): ")
		try:
			print rpc_connection.listreceivedbyaccount(mc, incemp)
		except:
			print rpc_connection.listreceivedbyaccount()
	except:
		print "\n---An error occurred---\n"

elif cmd == "listreceivedbyaddress":
	try:
		mc = raw_input("Minimum confirmations (optional): ")
		incemp = raw_input("Include empty? (true/false, optional): ")
		try:
			print rpc_connection.listreceivedbyaddress(mc, incemp)
		except:
			print rpc_connection.listreceivedbyaddress()
	except:
		print "\n---An error occurred---\n"

elif cmd == "listtransactions":
	try:
		acct = raw_input("Account (optional): ")
		count = raw_input("Number of transactions (optional): ")
		frm = raw_input("Skip (optional):")
		try:
			print rpc_connection.listtransactions(acct, count, frm)
		except:
			print rpc_connection.listtransactions()
	except:
		print "\n---An error occurred---\n"

elif cmd == "move":
	try:
		frm = raw_input("From: ")
		to = raw_input("To: ")
		amt = raw_input("Amount:")
		mc = raw_input("Minimum confirmations (optional): ")
		comment = raw_input("Comment (optional): ")
		try:
			print rpc_connection.move(frm, to, amt, mc, comment)
		except:
			print rpc_connection.move(frm, to, amt)
	except:
		print "\n---An error occurred---\n"

elif cmd == "sendfrom":
	try:
		frm = raw_input("From: ")
		to = raw_input("To: ")
		amt = raw_input("Amount:")
		mc = raw_input("Minimum confirmations (optional): ")
		comment = raw_input("Comment (optional): ")
		commentto = raw_input("Comment-to (optional): ")
		try:
			print rpc_connection.sendfrom(frm, to, amt, mc, comment, commentto)
		except:
			print rpc_connection.sendfrom(frm, to, amt)
	except:
		print "\n---An error occurred---\n"

elif cmd == "sendmany":
	try:
		frm = raw_input("From: ")
		to = raw_input("To (in format address1:amount1,address2:amount2,...): ")
		mc = raw_input("Minimum confirmations (optional): ")
		comment = raw_input("Comment (optional): ")
		try:
			print rpc_connection.sendmany(frm,to,mc,comment)
		except:
			print rpc_connection.sendmany(frm,to)
	except:
		print "\n---An error occurred---\n"

elif cmd == "sendtoaddress":
	try:
		to = raw_input("To (in format address1:amount1,address2:amount2,...): ")
		amt = raw_input("Amount:")
		comment = raw_input("Comment (optional): ")
		commentto = raw_input("Comment-to (optional): ")
		try:
			print rpc_connection.sendtoaddress(to,amt,comment,commentto)
		except:
			print rpc_connection.sendtoaddress(to,amt)
	except:
		print "\n---An error occurred---\n"

elif cmd == "setaccount":
	try:
		addr = raw_input("Address: ")
		acct = raw_input("Account:")
		print rpc_connection.setaccount(addr,acct)
	except:
		print "\n---An error occurred---\n"

elif cmd == "setgenerate":
	try:
		gen= raw_input("Generate? (true/false): ")
		cpus = raw_input("Max processors/cores (-1 for unlimited, optional):")
		try:
			print rpc_connection.setgenerate(gen, cpus)
		except:
			print rpc_connection.setgenerate(gen)
	except:
		print "\n---An error occurred---\n"

elif cmd == "settxfee":
	try:
		amt = raw_input("Amount:")
		print rpc_connection.settxfee(amt)
	except:
		print "\n---An error occurred---\n"

elif cmd == "stop":
	try:
		print rpc_connection.stop()
	except:
		print "\n---An error occurred---\n"

elif cmd == "validateaddress":
	try:
		addr = raw_input("Address: ")
		print rpc_connection.validateaddress(addr)
	except:
		print "\n---An error occurred---\n"

elif cmd == "walletpassphrase":
	try:
		pwd = raw_input("Enter wallet passphrase: ")
		rpc_connection.walletpassphrase(pwd, 60)
		print "\n---Wallet unlocked---\n"
	except:
		print "\n---An error occurred---\n"

elif cmd == "walletpassphrasechange":
	try:
		pwd = raw_input("Enter old wallet passphrase: ")
		pwd2 = raw_input("Enter new wallet passphrase: ")
		rpc_connection.walletpassphrasechange(pwd, pwd2)
		print
		print "\n---Passphrase changed---\n"
	except:
		print
		print "\n---An error occurred---\n"
		print

else:
	print "Command not found or not supported"
