import pickle
import os
import datetime
import getpass
import string

p=1

class user:
    pass

def new_user():
    
    print '----------------------------New Account----------------------------'
    while True:
        name=raw_input('Enter Your Name- ')
        print
        if len(name)>1:
            break
        else:
            print 'Name Too Short'
            print
            
    stat=1
    while stat==1:        
        try:
            f=open("account.txt","r")
            username=raw_input('Create A Username- ')
            print
            while True:
                c=pickle.load(f)
                if c.username==username:
                    print 'Username Is Taken'
                    print
                    stat=1
                    break
                else:
                    if len(username)<=1:
                        print 'Username Is Too Short'
                        print
                        stat=1
                        break
                    else:
                        stat=0
        except EOFError:
            f.close()
        except IOError:
            username=raw_input('Create A Username- ')
            print
            break
        
    password=raw_input('Create (Enter) A Password- ')
    print

    while True:
        confirm_pass=raw_input('Re-Enter (Confirm) Your Password- ')
        print
        if confirm_pass==password:
            print 'Your Password Is Confirmed'
            print
            break
        else:
            print 'Password Not Confirmed'
            print

    return (name,username,password)

def security():
    
    while True:
        
        print 'Pick Your Security Question'
        print
        print '----------------------------Security Questions----------------------------'
        print
        print '1)What is the last name of the teacher who gave you your first failing grade?'
        print '2)What is the name of your first pet?'
        print '3)What is the name of the first beach you visited?'
        print '4)What was your favorite place to visit as a child?'
        print '5)What was the make and model of your first car?'
        print '6)What was your maternal grandfather\'s first name?'
        print '7)In what city or town does your nearest sibling live?'
        print '8)Any Other (Custom)'
        print
        c=input('Enter Your Choice (Number)- ')
        if c==1:
            security_ques='What is the last name of the teacher who gave you your first failing grade?'
            print
            security_pas=raw_input('Enter Answer For The Security Question- ')
            break
        elif c==2:
            security_ques='What is the name of your first pet?'
            print
            security_pas=raw_input('Enter Answer For The Security Question- ')
            break
        elif c==3:
            security_ques='What is the name of the first beach you visited?'
            print
            security_pas=raw_input('Enter Answer For The Security Question- ')
            break
        elif c==4:
            security_ques='What was your favorite place to visit as a child?'
            print
            security_pas=raw_input('Enter Answer For The Security Question- ')
            break
        elif c==5:
            security_ques='What was the make and model of your first car?'
            print
            security_pas=raw_input('Enter Answer For The Security Question- ')
            break
        elif c==6:
            security_ques='What was your maternal grandfather\'s first name?'
            print
            security_pas=raw_input('Enter Answer For The Security Question- ')
            break
        elif c==7:
            security_ques='In what city or town does your nearest sibling live?'
            print
            security_pas=raw_input('Enter Answer For The Security Question- ')
            break
        elif c==8:
            security_ques=raw_input('Enter A Question Of Your Choice (Without \'?\')- ')
            print
            security_ques=security_ques+'?'
            security_pas=raw_input('Enter The Answer For The Security Question- ')
            break
        else:
            print 'Invalid Entry'

    return (security_ques,security_pas)
    
def user_details():
    
    while True:
        dob=raw_input('Enter Your Date Of Birth (D-M-Y)-  ')
        print
        try:
            if dob.count('-')==2 :
                d=dob.split('-')
                day=int(d[0])
                month=int(d[1])
                year=int(d[2])
                if datetime.datetime(year,month,day)<datetime.datetime.now():
                    if len(d[0])==1:
                        d[0]='0'+d[0]
                    if len(d[1])==1:
                        d[1]='0'+d[1]
                    if len(d[2])==1:
                        d[2]='000'+d[2]                    
                    elif len(d[2])==2:
                        d[2]='00'+d[2]
                    elif len(d[2])==3:
                        d[2]='0'+d[2]
                    dob=string.join(d,'-')
                    break
                else:
                    print 'Invalid DOB'
            else:
                print 'Invalid DOB'
                    
        except ValueError:
            print 'Invalid DOB'
            
    mobile_no=raw_input('Enter Your Mobile Number- ')
    print
    while True: 
        if len(mobile_no)==10 :
            stat=1
            for d in mobile_no:
                if d not in ['0','1','2','3','4','5','6','7','8','9']:
                    stat=0
                    print 'Invalid Mobile Number'
                    print
                    mobile_no=raw_input('Please Enter Valid Mobile Number- ')
                    print
                    break
        else:
            stat=0
            print 'Invalid Mobile Number'
            print
            mobile_no=raw_input('Please Enter Valid Mobile Number- ')
            print
            
        if stat==1:
            break

    email=raw_input('Enter Your Email ID- ')
    print
    while True:
        c_a=0
        c_dot=0
        for ch in email:
            if ch=='@':
                c_a=c_a+1
            elif ch=='.':
                c_dot=c_dot+1
        if '@' in email and '.' in email and c_a==1 and c_dot==1:
            mail=list(email.split('@'))
            ma=mail[1].split('.')
            if len(mail[0])>=1 and len(ma[0])>=1 and len(ma[1])>=2 and (' ' not in email):
                break
            else:
                print 'Invalid Email ID'
                email=raw_input('Please Enter a Valid Email ID- ')
                print
        else:
            print 'Invalid Email ID'
            email=raw_input('Please Enter a Valid Email ID- ')
            print

    print 'Note: Your Secret Code Is To Be Entered At The Choice Menu Of Your Inbox/Sent Messages In Order To View Your Private Messages'  
    print  
    scode=raw_input('Enter A 4 Digit Secret Code Starting with 0- ')
    print

    while True:
        if len(scode)!=4 or scode[0]!='0':
            print 'Invalid Code'
            scode=raw_input('Retry A 4 Digit Secret Code Starting with 0- ')
            print
        else:
            break
        
    status=raw_input('Enter Your Status- ')
    print
    
    return (dob,mobile_no,email,scode,status)

def encrypt(str,key):
    
    e=''
    for i in range(len(str)):      
        if i%2==0:
            if (ord(str[i])-key)<0:
                k=chr(254-(key-ord(str[i])))
            else:
                k=chr(ord(str[i])-key)
        else:
            if (ord(str[i])+key)>254:
                k=chr(ord(str[i])+key-254)
            else:
                k=chr(ord(str[i])+key)
        e=e+k        
    return(e)

def decrypt (str,key):
    
    d=''      
    for i in range(len(str)):
        if i%2==0:
            if (ord(str[i])+key)>254:
                k=chr(ord(str[i])+key-254)
            else:
                k=chr(ord(str[i])+key)                
        else:
            if (ord(str[i])-key)<0:
                k=chr(254-(key-ord(str[i])))
            else:
                k=chr(ord(str[i])-key)                
        d=d+k
    return(d)

def storedata(account,details,security):
    
    f=open('account.txt','a')
    s=user()
    s.name=account[0]
    s.username=account[1]
    s.password=account[2]
    s.security_ques=security[0]
    s.security_ans=security[1]
    s.dob=details[0]
    s.mobile=details[1]
    s.email=details[2]
    s.scode=details[3]
    s.status=details[4]
    s.friends=[]
    s.sent=[]
    s.received=[]
    s.psent=[]
    s.preceived=[]
    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        print '----------------Account Details----------------'
        print 'Name:',s.name
        print 'Username:',s.username
        print 'Password:',s.password
        print 'Date Of Birth (D-M-Y):',s.dob
        print 'Email:',s.email
        print 'Mobile:',s.mobile
        print 'Secret Code:',s.scode
        print 'Status:',s.status
        print 'Security Question:',s.security_ques
        print 'Security Answer:',s.security_ans
        print '--------------------------------------------------'
        choice=raw_input('Do You Want To Confirm Creating This Account (y/n)- ')
        if choice.lower() in ['y','n']:
            break
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print 'Invalid Choice'            
    if choice.lower()=='y':
        pickle.dump(s,f)
        os.system('cls' if os.name == 'nt' else 'clear')
        print 'Account Created Successfuly'
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print 'Account Not Created'
    f.close()
        
def key(user1,user2):
    
    f=open('account.txt','r')
    s=0
    try:
        c=pickle.load(f)
        if c.username==user1 or c.username==user2:
            for n in c.dob:
                if n!='-':
                    s=s+int(n)
    except EOFError:
        f.close()

    while len(str(s))>2:
        s=s/7
    return (s)

def find_friends(friend,user,userfriends):
    stat=1
    f=open('account.txt','r')
    try:
        while True:
            c=pickle.load(f)
            if (c.username==friend or c.email==friend) and c.username!=user:
                print 'We Have Found Your Friend'
                print 'Name:',c.name
                print 'Email:',c.email
                mut=mutual(userfriends,friend)
                if mut!=[]:
                    print 'Mutual Friends:',
                    for i in range(len(mut)):
                        if i!=(len(mut)-1):
                            print (mut[i]+','),
                        else:
                            print mut[i]
                else:   
                    print 'No Mutual Friends'
                    
                while True:
                    choice=raw_input('Do You Want To Add Him/Her (y/n)- ')
                    os.system('cls' if os.name == 'nt' else 'clear')
                    if choice.lower() in ['y','n']:
                        break
                    else:
                        print 'Invalid Choice'
                return(choice)
            else:           
                stat=0
    except EOFError:
        f.close()
    if stat==0:
        os.system('cls' if os.name == 'nt' else 'clear')
        print 'Invalid Friend'
        return ('-1')
        
def mutual(userfriends,friend):
    f=open('account.txt','r')
    mut=[]
    try:
        while True:
            c=pickle.load(f)
            if c.username in userfriends:
                for i in c.friends:
                    if i==friend:
                        mut.append(c.username)
    except EOFError:
        f.close()
        return(mut)                          
                       
def friends(user):
    friend=raw_input('Enter Username Of Person- ')
    f=open('account.txt','r')
    choice='n'
    try:
        while True:
            c=pickle.load(f)
            if c.username==user:
                if c.friends!=[]:                    
                    if friend in c.friends:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print 'This User Is Already Your Friend'
                    else:
                        choice=find_friends(friend,user,c.friends)                        
                else:                    
                    choice=find_friends(friend,user,c.friends)
    except EOFError:
        f.close()
        
    if choice.lower()=='y':
        f1=open('account.txt','r')
        f2=open('newfile.txt','w')
        try:
            while True:
                c=pickle.load(f1)
                if c.username==user:
                    c.friends.append(friend)
                elif c.username==friend:
                    c.friends.append(user)
                pickle.dump(c,f2)
        except EOFError:
            f1.close()
            f2.close()            
        os.remove('account.txt')
        os.rename('newfile.txt','account.txt')
        print 'You Have Successfuly Added This User'

def inbox(user,msgs,pmsg,code):

    while True:
        print '----------------------Inbox---------------------'
        print '<~>-Unread                          <>-Read'
        for i in range(len(msgs)):
            if msgs[i][3]==1:
                k=key(user,msgs[i][0])+3
                m=decrypt(msgs[i][1],k)
                if msgs[i][2]==0:
                    print str(i+1)+')'+msgs[i][0]+':\''+m[:21]+'\'<~>'
                else:
                    print str(i+1)+')'+msgs[i][0]+':\''+m[:21]+'\'<>'
            else:
                if msgs[i][2]==0:
                    print str(i+1)+')'+msgs[i][0]+':\''+msgs[i][1][:21]+'\'<~>'
                else:
                    print str(i+1)+')'+msgs[i][0]+':\''+msgs[i][1][:21]+'\'<>'
        print str(len(msgs)+1)+')Return To Menu'
        c=raw_input('Enter Choice- ')
        os.system('cls' if os.name == 'nt' else 'clear')
        ch=int(c)
        if ch in range(1,(len(msgs)+2)) or c==code:
            break
        else:
            print 'Invalid Entry'
    if c==code:
        if pmsg!=[]:
            while True:
                print '----------------------Private Inbox---------------------'
                print '<~>-Unread                          <>-Read'
                for i in range(len(pmsg)):
                    k=key(user,pmsg[i][0])+3
                    m=decrypt(pmsg[i][1],k)
                    if pmsg[i][2]==0:
                        print str(i+1)+')'+pmsg[i][0]+':\''+m[:21]+'\'<~>'
                    else:
                        print str(i+1)+')'+pmsg[i][0]+':\''+m[:21]+'\'<>'
                print str(len(pmsg)+1)+')Return To Menu'
                ch=input('Enter Choice- ')
                os.system('cls' if os.name == 'nt' else 'clear')
                if ch in range(1,(len(pmsg)+2)):
                    break
                else:
                    print 'Invalid Entry'

            if ch==(len(pmsg)+1):
                pass
            else:
                k=key(user,pmsg[ch-1][0])+3
                m=decrypt(pmsg[ch-1][1],k)
                print
                print pmsg[ch-1][0]+':\''+m+'\''
                print
                updatemsg(user,2,pmsg[ch-1][4],ch)
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print 'You Have Nothing Private'
        
    elif ch==(len(msgs)+1):
        pass
    else:
        if msgs[ch-1][3]==1:
            k=key(user,msgs[ch-1][0])+3
            m=decrypt(msgs[ch-1][1],k)
            print
            print msgs[ch-1][0]+':\''+m+'\''
            print
            updatemsg(user,1,ch)
        else:
            print
            print msgs[ch-1][0]+':\''+msgs[ch-1][1]+'\''
            print

def sentmsg(user,msgs,pmsg,code):
    while True:
        print '----------------------Sent---------------------'
        for i in range(len(msgs)):
            if msgs[i][3]==1:
                k=key(user,msgs[i][0])+3
                m=decrypt(msgs[i][1],k)
                print str(i+1)+')'+msgs[i][0]+':\''+m[:21]+'\''
            else:
                print str(i+1)+')'+msgs[i][0]+':\''+msgs[i][1][:21]+'\''
                
        print str(len(msgs)+1)+')Return To Menu'
        c=raw_input('Enter Choice- ')
        os.system('cls' if os.name == 'nt' else 'clear')
        ch=int(c)
        if ch in range(1,(len(msgs)+2)) or c==code:
            break
        else:
            print 'Invalid Entry'
    if c==code:
        if pmsg!=[]:
            while True:
                print '----------------------Private Sent---------------------'
                for i in range(len(pmsg)):
                    k=key(user,pmsg[i][0])+3
                    m=decrypt(pmsg[i][1],k)
                    print str(i+1)+')'+pmsg[i][0]+':\''+m[:21]+'\''
                print str(len(pmsg)+1)+')Return To Menu'
                ch=input('Enter Choice- ')
                os.system('cls' if os.name == 'nt' else 'clear')
                if ch in range(1,(len(pmsg)+2)):
                    break
                else:
                    print 'Invalid Entry'
            if ch==(len(pmsg)+1):
                pass
            else:
                k=key(user,pmsg[ch-1][0])+3
                m=decrypt(pmsg[ch-1][1],k)
                print
                print pmsg[ch-1][0]+':\''+m+'\''
                print

        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print 'You Have Nothing Private'
    elif ch==(len(msgs)+1):
        pass
    else:
        if msgs[ch-1][3]==1:
            k=key(user,msgs[ch-1][0])+3
            m=decrypt(msgs[ch-1][1],k)
            print
            print msgs[ch-1][0]+':\''+m+'\''
            print
        else:
            print
            print msgs[ch-1][0]+':\''+msgs[ch-1][1]+'\''
            print

def updatemsg(user,choice,ch1,ch2=0):
    f1=open('account.txt','r')
    f2=open('newfile.txt','w')
    try:
        while True:
            c=pickle.load(f1)
            if c.username==user:               
                if choice==1:
                    c.received[ch1-1][2]=1
                else:
                    c.received[ch1-1][2]=1
                    c.preceived[ch2-1][2]=1
                pickle.dump(c,f2)
            else:
                pickle.dump(c,f2)
    except EOFError:
        f1.close()
        f2.close()
    os.remove('account.txt')
    os.rename('newfile.txt','account.txt')

def displaymsg(user,choice):                 
    f=open('account.txt','r')
    try:
        while True:
            c=pickle.load(f)
            if c.username==user:
                if choice==1:
                    received=c.received
                    preceived=c.preceived
                    scode=c.scode
                else:
                    sent=c.sent
                    psent=c.psent
                    scode=c.scode

    except EOFError:
        f.close()
    if choice==1:
        if received!=[]:
            inbox(user,received,preceived,scode)
        else:
            print 'You Have No Messages'
    else:
        if sent!=[]:
            sentmsg(user,sent,psent,scode)
        else:
            print 'You Have No Sent Messages'
                                          
def message(user):
    
    friends=dispfriends(user,1)
    if friends!=[]:    
        while True:
            print '-------------Messaging-------------'
            print '1)Normal Message'
            print '2)Private Message'
            choice=input('Enter Your Choice- ')
            os.system('cls' if os.name == 'nt' else 'clear')
            if choice in [1,2]:
                break
            else:
                print 'Invalid Entry'
        dispfriends(user)
        while True:
            ch=input('Enter Your Choice- ')
            os.system('cls' if os.name == 'nt' else 'clear')
            if ch in range(1,(len(friends)+1)):
                break
            else:
                print 'Invalid Choice'
        
        friend=friends[ch-1]
        msg=raw_input('Enter Message- ')     
        f1=open('account.txt','r')
        f2=open('newfile.txt','w')
        k=key(user,friend)+3
        try:
            while True:
                c=pickle.load(f1)
                if c.username==user:
                    if choice==2:
                        c.psent.append([friend,encrypt(msg,k),0,choice,(len(c.sent)+1)])
                    c.sent.append([friend,encrypt(msg,k),0,choice])
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print 'Your Message Has Been Sent'
                elif c.username==friend:
                    if choice==2:
                        c.preceived.append([user,encrypt(msg,k),0,choice,(len(c.received)+1)])
                    c.received.append([user,encrypt(msg,k),0,choice])
                pickle.dump(c,f2)
        except EOFError:
            f1.close()
            f2.close()
        os.remove('account.txt')
        os.rename('newfile.txt','account.txt')
    else:
        print 'You Have No Friends To Message'
        
def updatedetails(user):
    while True:
        print '-------------Update Details-------------'
        print '1)Email ID'
        print '2)Mobile Number'
        print '3)Secret Code'
        print '4)Return To Menu'
        choice=input('Enter Your Choice- ')
        os.system('cls' if os.name == 'nt' else 'clear')
        if choice in range(1,5):
            break
        else:
            print 'Invalid Entry'
            
    f1=open('account.txt','r')
    f2=open('newfile.txt','w')

    try:
        while True:
            c=pickle.load(f1)
            if c.username==user:
                if choice==1:
                    email=raw_input('Enter Your Email ID- ')
                    while True:
                        c_a=0
                        c_dot=0
                        for ch in email:
                            if ch=='@':
                                c_a=c_a+1
                            elif ch=='.':
                                c_dot=c_dot+1
                        if '@' in email and '.' in email and c_a==1 and c_dot==1:
                            mail=list(email.split('@'))
                            ma=mail[1].split('.')
                            if len(mail[0])>=1 and len(ma[0])>=1 and len(ma[1])>=2 and (' ' not in email):
                                break
                            else:
                                print 'Invalid Email ID'
                                email=raw_input('Please Enter a Valid Email ID- ')                                
                        else:
                            print 'Invalid Email ID'
                            email=raw_input('Please Enter a Valid Email ID- ')
                    c.email=email
                    print 'Successfuly Updated Email'
                    
                elif choice==2:
                    mobile_no=raw_input('Enter Your Mobile Number- ')
                    while True: 
                        if len(mobile_no)==10 :
                            stat=1
                            for d in mobile_no:
                                if d not in ['0','1','2','3','4','5','6','7','8','9']:
                                    stat=0
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    print 'Invalid Mobile Number'
                                    mobile_no=raw_input('Please Enter Valid Mobile Number- ')
                                    break
                        else:
                            stat=0
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print 'Invalid Mobile Number'
                            mobile_no=raw_input('Please Enter Valid Mobile Number- ')                            
                        if stat==1:
                            print 'Successfuly Update Mobile Number'
                            break

                elif choice==3:
                    scode=raw_input('Enter A 4 Digit Secret Code Starting with 0- ')
                    while True:
                        if len(scode)==4 and scode[0]=='0':
                            break
                        else:
                            print 'Invalid Code'
                            scode=raw_input('Retry A 4 Digit Secret Code Starting with 0- ')
                    c.scode=scode
                    print 'Successfuly Updated Secret Code'
                else:
                    pass

            pickle.dump(c,f2)
            
    except EOFError:
        f1.close()
        f2.close()
    os.remove('account.txt')
    os.rename('newfile.txt','account.txt')

def login(st):
    global en
    global p
    d={}
    try:
        f=open('account.txt','r')
        while True:            
            s=pickle.load(f)
            d[s.username]=s.password

    except IOError:
        print 'No Existing Accounts\''
        
    except EOFError:
        f.close()
        if p==1:
            en=st
        if st>=en or p==1:
            p=-1
            c=0
            username=raw_input('Enter Username- ')
            while True:
                if username in d:
                    password=getpass.getpass('Enter Password- ')
                    while True:                        
                        if password==d[username]:
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print 'You Are Signed In'
                            return(username,password)
                        else:
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print 'Incorrect Password'
                            c+=1
                            if c>=3:
                                print 'If You Forgot Your Password, Please Use The Forgot Password Function'
                                en=datetime.datetime.now()+datetime.timedelta(0,30)
                                st=datetime.datetime.now()
                                return(en)
                            while True:
                                print '1)Retype Password'
                                print '2)Change Username'
                                print '3)Return To Main Menu'
                                choice=input('Enter Your Choice- ')
                                if choice==1:
                                    password=getpass.getpass('Re-Enter Password- ')
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    break
                                elif choice==2:
                                    break
                                elif choice==3:
                                    return(None)
                                else:
                                    print 'Invalid Entry'
                                    break
                        if choice==2:
                            username=raw_input('Enter Another Username- ')
                            os.system('cls' if os.name == 'nt' else 'clear')
                            break
                else:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print 'Invalid Username'
                    c+=1
                    if c>=3:
                        en=datetime.datetime.now()+datetime.timedelta(0,30)
                        st=datetime.datetime.now()
                        return(en)
                    while True:
                        print '1)Retype Username'
                        print '2)Return To Main Menu'
                        choice=input('Enter Your Choice- ')
                        if choice==1:
                            username=raw_input('Enter Another Username- ')
                            os.system('cls' if os.name == 'nt' else 'clear')
                            break
                        elif choice==2:
                            return(None)
                        else:
                            print 'Invalid Entry'                
        else:
            return(en)
        
def status(user):
    print '-----------Status-----------'
    print
    f1=open('account.txt','r')
    f2=open('newfile.txt','w')
    try:
        while True:
            c=pickle.load(f1)
            if c.username==user:
                print 'Status:',c.status
                print
                if raw_input('Do You Want To Change Status (y/n)- ').lower()=='y':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    c.status=raw_input('Enter New Status- ')
                    print
                    print 'Status Successfuly Changed'
                    print
                else:
                    os.system('cls' if os.name == 'nt' else 'clear')
            pickle.dump(c,f2)
            
    except EOFError:
        f1.close()
        f2.close()
    os.remove('account.txt')
    os.rename('newfile.txt','account.txt')

def displayfriends(user):
    friends=dispfriends(user,1)
    if friends!=[]:
        while True:
            print '------------------Friends------------------'
            for i in range(len(friends)):
                print str(i+1)+')'+friends[i]
            ch=input('Enter Your Choice- ')
            os.system('cls' if os.name == 'nt' else 'clear')
            if ch in range(1,(len(friends)+1)):
                break
            else:
                print 'Invalid Entry'
        f=open('account.txt','r')
        try:
            while True:
                c=pickle.load(f)
                if c.username==friends[ch-1]:
                    print
                    print 'Name:',c.name
                    print 'Date Of Birth (D/M/Y):',c.dob
                    print 'Email:',c.email
                    print 'Mobile:',c.mobile
                    print 'Friends:',
                    for i in range(len(c.friends)):                        
                        if i!=(len(c.friends)-1):
                            print (c.friends[i]+','),
                        else:
                            print c.friends[i]
                    mut=mutual(friends,friends[ch-1])
                    if mut!=[]:
                        print 'Mutual Friends:',
                        for i in range(len(mut)):
                            if i!=(len(mut)-1):
                                print (mut[i]+','),
                            else:
                                print mut[i]
                    else:   
                        print 'No Mutual Friends'                                            
                    print 'Status:',c.status
                    print
        except EOFError:
            f.close()
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print 'You Have No Friends'
        
def dispfriends(user,choice=-1):
    f=open('account.txt','r')
    try:
        while True:
            c=pickle.load(f)
            if c.username==user:
                friends=c.friends
    except EOFError:
        f.close()
    if choice==-1:
        if friends!=[]:
            print '------------Friends------------'
            for i in range(len(friends)):
                print str(i+1)+')'+friends[i]
        else:
            print 'You Have No Friends'
    else:
        return(friends)

def del_friends(user):
    friends=dispfriends(user,1)    
    if friends!=[]:
        while True:
            dispfriends(user)
            print str(len(friends)+1)+')Return To Menu'
            choice=input('Enter Your Choice- ')
            os.system('cls' if os.name == 'nt' else 'clear')
            if choice in range(1,len(friends)+2):
                break
            else:
                print 'Invalid Entry'
        if choice!=(len(friends)+1):
            f1=open('account.txt','r')
            f2=open('newfile.txt','w')
            try:
                while True:
                    c=pickle.load(f1)
                    if c.username==user:
                        del c.friends[choice-1]
                    elif c.username==friends[choice-1]:
                        c.friends.remove(user)
			print 'You Have Successfuly Deleted Your Friend'
                    pickle.dump(c,f2)
            except EOFError:
                f1.close()
                f2.close()
            os.remove('account.txt')
            os.rename('newfile.txt','account.txt')
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print 'No Friends Deleted'
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print 'You Have No Friends'
        

def forgot_pass():  
    try:
        stat=0
        f=open('account.txt','r')
        username=raw_input('Enter Your Username- ')
        while True:
            c=pickle.load(f)
            if c.username==username:
                ans=raw_input(c.security_ques+'- ')
                if ans==c.security_ans:
                    print 'Password:',c.password
                else:
                    print 'Wrong Answer'
                stat=1                    
    except EOFError:
        f.close()
    except IOError:
        print 'No Existing Accounts\''
    if stat==0:
        print 'Invalid Username'
        
def admin_login():
    username=raw_input('Enter Username- ')
    if username=='Mescure':
        password=getpass.getpass('Enter The Password- ')
        if password=='mescure123':
            print 'Welcome Admin'
            return('Y')
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print 'Invalid Password'
            return('N')
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print 'Invalid Username'
        return('N')        

def dispaccounts(choice=-1):
        f=open('account.txt','r')
        try:
            i=0
            print '-------------------------------------------------'
            while True:
                c=pickle.load(f)
                i=i+1
                print '-------------------User '+str(i)+'-------------------'
                print 'Name:',c.name
                print 'Date Of Birth (D-M-Y):',c.dob
                print 'Username:',c.username
                print 'Email:',c.email
                print 'Mobile:',c.mobile
                print 'Friends:',
                for j in range(len(c.friends)):                        
                    if j!=(len(c.friends)-1):
                        print (c.friends[j]+','),
                    else:
                        print c.friends[j]
                print 'Status:',c.status
                print '-------------------------------------------------'

        except EOFError:
            f.close()
        if choice==1:
            return (i)
        
def view_details(user):
    f=open('account.txt','r')
    try:
        while True:
            c=pickle.load(f)
            if c.username==user:
                print '-----------------------Details-----------------------'
                print 'Name:',c.name
                print 'Date Of Birth (D-M-Y):',c.dob
                print 'Mobile Number:',c.mobile
                print 'Email ID',c.email
    except EOFError:
        f.close()

def deletemsg(user):
    f1=open('account.txt','r')
    f2=open('newfile.txt','w')
    choice=1
    while True:
        print '--------------Delete Message--------------'
        print '1)Inbox'
        print '2)Sent Messages'
        choice=input('Enter Your Choice- ')
        os.system('cls' if os.name == 'nt' else 'clear')
        if choice in range(1,3):
            break
        else:
            print 'Invalid Entry'
                    
    try:
        while True:
            c=pickle.load(f1)
            if c.username==user:
                if choice==1:
                    msgs=c.received
                    if msgs!=[]:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        while True:
                            print '----------------------Inbox---------------------'
                            print '<~>-Unread                          <>-Read'                    
                            for i in range(len(msgs)):
                                if msgs[i][3]==1:
                                    k=key(user,msgs[i][0])+3
                                    m=decrypt(msgs[i][1],k)
                                    if msgs[i][2]==0:
                                        print str(i+1)+')'+msgs[i][0]+':\''+m[:21]+'\'<~>'
                                    else:
                                        print str(i+1)+')'+msgs[i][0]+':\''+m[:21]+'\'<>'
                                else:
                                    if msgs[i][2]==0:
                                        print str(i+1)+')'+msgs[i][0]+':\''+msgs[i][1][:21]+'\'<~>'
                                    else:
                                        print str(i+1)+')'+msgs[i][0]+':\''+msgs[i][1][:21]+'\'<>'
                            print str(len(msgs)+1)+')Return To Menu'
                            ch=input('Enter Choice- ')
                            os.system('cls' if os.name == 'nt' else 'clear')
                            if ch in range(1,len(msgs)+2):
                                break
                            else:
                                print 'Invalid Entry'
                        if ch!=(len(msgs)+1):
                            if msgs[ch-1][3]==2:
                                for i in range(len(msgs)):
                                    if i>(ch-1):
                                        for j in range(len(c.preceived)):
                                            if c.preceived[j][4]>(ch-1):
                                                c.preceived[j][4]-=1
                                for i in c.preceived:                                    
                                    if i[4]==(ch-1):
                                        c.preceived.remove(i)                  
                            del msgs[ch-1]
                            print 'Your Message Has Been Deleted Successfuly'
                    else:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print 'You Have No Messages'
                if choice==2:
                    msgs=c.sent
                    if msgs!=[]:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        while True:
                            print '----------------------Sent---------------------'
                            for i in range(len(msgs)):
                                if msgs[i][3]==1:
                                    k=key(user,msgs[i][0])+3
                                    m=decrypt(msgs[i][1],k)
                                    print str(i+1)+')'+msgs[i][0]+':\''+m[:21]+'\''
                                else:
                                    print str(i+1)+')'+msgs[i][0]+':\''+msgs[i][1][:21]+'\''                                
                            print str(len(msgs)+1)+')Return To Menu'
                            ch=input('Enter Choice- ')
                            os.system('cls' if os.name == 'nt' else 'clear')
                            if ch in range(1,len(msgs)+2):
                                break
                            else:
                                print 'Invalid Entry'
                        if ch!=(len(msgs)+1):
                            if msgs[ch-1][3]==2:
                                for i in range(len(msgs)):
                                    if i>(ch-1):
                                        for j in range(len(c.preceived)):
                                            if c.psent[j][4]>(ch-1):
                                                c.psent[j][4]-=1
                                for i in c.psent:
                                    if i[4]==(ch-1):
                                        c.psent.remove(i)                                    
                            del msgs[ch-1]
                            print 'Your Message Has Been Deleted Successfuly'
                    else:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print 'You Have No Sent Messages'
            pickle.dump(c,f2)    
                    
    except EOFError:
        f1.close()
        f2.close()
    os.remove('account.txt')
    os.rename('newfile.txt','account.txt')

def delaccounts():

    while True:
        n=dispaccounts(1)
        print str(n+1)+')Return To Menu'
        choice=input('Enter Your Choice- ')
        os.system('cls' if os.name == 'nt' else 'clear')
        if choice in range(1,n+2):
            break
        else:
            print 'Invalid Entry'
    if choice!=(n+1):        
        f=open('account.txt','r')
        try:
            i=0
            while True:
                c=pickle.load(f)
                i=i+1
                if i==choice:
                    user=c.username
        except EOFError:
            f.close()
        f1=open('account.txt','r')
        f2=open('newfile.txt','w')
        try:
            while True:
                c=pickle.load(f1)
                if user in c.friends:
                    c.friends.remove(user)
                    
                if c.username!=user:
                    pickle.dump(c,f2)
                else:
                    print 'You Have Successfuly Deleted This User'
        except EOFError:
            f1.close()
            f2.close()
        os.remove('account.txt')
        os.rename('newfile.txt','account.txt')            
            
'''
f=open('account.txt','w')
s1=user()
s2=user()
s1.username='tevin'
s1.password='tevin123'
s1.security_ques='Wbb'
s1.security_ans='tevin'
s1.name='Tevin'
s1.mobile='0507551871'
s1.email='tevinjose97@gmail.com'
s1.scode='0324'
s1.status='thug life'
s1.friends=[]
s1.sent=[]
s1.received=[]
s1.psent=[]
s1.preceived=[]
s1.dob='16-11-1997'
s2.username='tino'
s2.password='tino123'
s2.security_ques='Wbb'
s2.security_ans='tino'
s2.name='Tino'
s2.mobile='0501234567'
s2.email='tinojose97@gmail.com'
s2.scode='0416'
s2.status='cunt life'
s2.friends=[]
s2.sent=[]
s2.received=[]
s2.psent=[]
s2.preceived=[]
s2.dob='11-11-1997'
pickle.dump(s1,f)
pickle.dump(s2,f)
f.close()
'''
while True:        
    print '-----------------Mescure-----------------'
    print '1)Login (Existing User)'
    print '2)Create New Account'
    print '3)Forgot Password'
    print '4)Admin Login'
    print '5)Developers'
    print '6)Exit'

    choice=input('Enter Your Choice- ')
    if choice==1:
        os.system('cls' if os.name == 'nt' else 'clear')
        st=datetime.datetime.now()
        usern=login(st)        
        while True:
            if type(usern)==datetime.datetime:
                t=str(en-datetime.datetime.now())[5:7]
                print 'Sorry, Please Try Again In',t,'Seconds'
                break
            elif usern!=None:
                username=usern[0]
                password=usern[1]
                print '-------------------Welcome '+usern[0]+'-------------------'
                print '1)Inbox'
                print '2)Sent Messages'
                print '3)Compose Message'
                print '4)Delete Message'
                print '5)Status'
                print '6)Find And Add Friends'
                print '7)View Friends'
                print '8)Delete Friends'
                print '9)View Details'
                print '10)Update Account'
                print '11)Logout And Return To Main Menu'
                while True:                
                    c=input('Enter Your Choice- ')
                    os.system('cls' if os.name == 'nt' else 'clear')
                    if c in range(1,12):
                        break
                    else:
                        print 'Invalid Entry'        
                if c==1:
                    displaymsg(username,1)
                elif c==2:
                    displaymsg(username,2)
                elif c==3:
                    message(username)
                elif c==4:
                    deletemsg(username)
                elif c==5:
                    status(username)
                elif c==6:
                    friends(username)
                elif c==7:
                    displayfriends(username)
                elif c==8:
                    del_friends(username)
                elif c==9:
                    view_details(username)
                elif c==10:
                    updatedetails(username)
                else:
                    break
            else:
                print 'Login Unsuccessful'
                break
            
    elif choice==2:
        os.system('cls' if os.name == 'nt' else 'clear')
        storedata(new_user(),user_details(),security())
        
    elif choice==3:
        os.system('cls' if os.name == 'nt' else 'clear')
        forgot_pass()
        
    elif choice==4:
        os.system('cls' if os.name == 'nt' else 'clear')
        if admin_login()=='Y':
            os.system('cls' if os.name == 'nt' else 'clear')
            while True:
                print '-----------------Administrator-----------------'
                print '1)Display Accounts'
                print '2)Delete Accounts'
                print '3)Logout And Return To Main Menu'
                ch=input('Enter Your Choice- ')
                os.system('cls' if os.name == 'nt' else 'clear')
                if ch==1:
                    dispaccounts()
                elif ch==2:
                    delaccounts()
                elif ch==3:
                    break
                else:
                    print 'Invalid Entry'
        else:
            print 'Sorry, You Are Not Privilleged To Access This Content'
            
    elif choice==5:
        os.system('cls' if os.name == 'nt' else 'clear')
        print 'A Creation Of,'
        print ' ___________________________________________' 
        print '         |         |             |'
        print '         |         |             |' 
        print '         |         |_____        |'
        print '         |               |       |'
        print '         |EVIN           |HAUN   |INO'
        print '         |          _____|       |        STUDIOS'
        print 
        print 'Copyright Protected (c)'

    elif choice==6:
        exit()
        
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print 'Invalid Entry'
