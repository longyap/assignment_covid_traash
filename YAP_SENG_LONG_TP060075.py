
#YAP SENG LONG
#TP060075

#----------------------------------------------------------------------------new pat id----------------------------------------------------------------------------------------
def patient_detail():
    def pat_id_gen():
        pat_id_gen =open ('pat_id_gen.txt','a')
        pat_id_gen.write('\n1')
        pat_id_gen.close()

        pat_id_gen_cnt=0
        pat_id_gen2=open('pat_id_gen.txt','r')
        pat_idgen_r= pat_id_gen2.read()
        chk_list = pat_idgen_r.split('\n') 
        for no in chk_list:
            if no :
                pat_id_gen_cnt+=1
            else:
                pat_id_gen.close()
        return pat_id_gen_cnt


    name = input('Enter patient name: ')
    gndr = input('Enter patient gender (M/F/X): ')
    bld_typ=input('Enter patient blood type (A+-/B+-/AB+-/O+-): ')
    fone = input('Enter patient phone number: ')
    zon_inpt=  input("Enter patient's zone (A/B/C/D): ")
    g_cod= input('Enter group code (ATO/ACC/AEO/SID/AHS): ')
    if (zon_inpt=='A'or zon_inpt=='a'):
        zon_represent='!'
    elif(zon_inpt=='B'or zon_inpt=='b'):
        zon_represent='@'
    elif(zon_inpt=='C'or zon_inpt=='c'):
        zon_represent='#'
    elif(zon_inpt=='D'or zon_inpt=='d'):
        zon_represent='$'
    patient_reg = open('Patient_id.txt','a')
    pat_id_gen = str (pat_id_gen())
    pat_id= ''.join([gndr,pat_id_gen,g_cod,zon_represent])
    patient_reg.write('\n'+pat_id+'\t\t'+name+'\t'+gndr+'\t'+bld_typ+'\t\t'+fone+'\t'+zon_inpt+'\t'+g_cod)
    print('\n\nPatient',name,'(',pat_id,') has been registered successfully')
    patient_reg.close()


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++    
#---------------------------------------New test record-----------------------------------------------------
    
def new_tes_rec1():

    pat_id = input('Enter patient ID:')
    tes_reslt=input('Enter test result (P/N):')

    if (tes_reslt=='P' or tes_reslt=='p' ):
        act_tk= input ('Action Taken (QHNF/HQNF): ')
        if (act_tk=='QHNF' or act_tk=='qhnf'):
            h_act_tk= input('Hospitalize action taken(NW /ICU):')
        else:
            h_act_tk= 'n/a'
        pat_status_active_gen(pat_id)
        patient_tes_reg = open('Test1_positive.txt','a')
        patient_tes_reg.write('\n\t'+pat_id+'\t\t'+act_tk+'\t\t'+h_act_tk)
    else:
        act_tk= input ('Action Taken (QDFR/HQFR/CWFR): ')
        h_act_tk= 'n/a'
        patient_tes_reg = open('Test1_negative.txt','a')
        patient_tes_reg.write('\n\t'+pat_id+'\t\t'+act_tk+'\t\t'+h_act_tk)
    print('\n\nPatient ID '+pat_id+' has been recorded in T1 successfully')
    patient_tes_reg.close()

def new_tes_chk_rec2():#nested function
    def new_tes_rec2():

      tes_reslt=input('Enter test result (P/N):')
      

      if(tes_reslt=='P' or tes_reslt=='p'):
        act_tk= input ('Action Taken (QHNF/HQNF): ')
        if (act_tk=='QHNF'or act_tk=='qhnf'):
            h_act_tk= input('Hospitalize action taken(NW /ICU):')
        else:
            h_act_tk= 'n/a'            
        pat_status_active_gen(pat_id)
        patient_tes_reg = open('Test2_positive.txt','a')
        patient_tes_reg.write('\n\t'+pat_id+'\t\t'+act_tk+'\t\t'+h_act_tk)
      else:
            act_tk= input ('Action Taken (QDFR/HQFR/CWFR): ')
            h_act_tk= 'n/a'
            patient_tes_reg = open('Test2_negative.txt','a')
            patient_tes_reg.write('\n\t'+pat_id+'\t\t'+act_tk+'\t\t'+h_act_tk)
  
      print('\n\nPatient ID '+pat_id+' has been recorded in T2 successfully')
      patient_tes_reg.close()
      
    pat_id_chk = open('Test1_negative.txt','r')
    pat_id = input('Enter patient ID:')
    for line in pat_id_chk:
        line =line.rstrip()
        if not pat_id in line:
            continue
        else:
           new_tes_rec2()
           break
    else:
        print('\nPatient ID',pat_id,'may have been tested positive or not yet recorded on previous test')




def new_tes_chk_rec3():#nested function
    def new_tes_rec3():
        tes_reslt=input('Enter test result (P/N):')
   
    
        if(tes_reslt=='P'or tes_reslt=='p'):
            act_tk= input ('Action Taken (QHNF/HQNF): ')
            if (act_tk=='QHNF' or act_tk=='qhnf'):
                h_act_tk= input('Hospitalize action taken(NW /ICU):')
            else:
                h_act_tk= 'n/a'  
            pat_status_active_gen(pat_id)
            patient_tes_reg = open('Test3_positive.txt','a')
            patient_tes_reg.write('\n\t'+pat_id+'\t\t'+act_tk+'\t\t'+h_act_tk)
        else:
            act_tk= input ('Action Taken (RU/CW): ')
            h_act_tk= 'n/a'  
            patient_tes_reg = open('Test3_negative.txt','a')
            patient_tes_reg.write('\n\t'+pat_id+'\t\t'+act_tk+'\t\t'+h_act_tk)
        print('\n\nPatient ID '+pat_id+'('+tes_reslt+') has been recorded in T3 successfully')
        patient_tes_reg.close()

    pat_id_chk = open('Test2_negative.txt','r+')
    pat_id = input('Enter patient ID:')
    for line in pat_id_chk:
        line =line.rstrip()
        if not pat_id in line:
            continue
        else:
           new_tes_rec3()
           break
    else:
        print('\n\nPatient ID'+pat_id+'may have been tested positive or not yet recorded on previous test')


#*****************************************************************************************************************************
#-------------------------------------------------------new status-----------------------------------------------------------------
#*************************************************************************************************************************************
def pat_status_active():
    pat_id = input ('Enter Patient ID: ')
    pat_status_active_gen(pat_id)




def pat_status_recovered():
  
    pat_id =input ('Enter Patient ID: ')
    def case_id_gen(): 
        case_id_gen =open ('case_id_rec_gen.txt','a')
        case_id_gen.write('\na')
        case_id_gen.close()

        case_id_gen_cnt=0
        case_id_gen2=open('case_id_rec_gen.txt','r')
        case_idgen_r= case_id_gen2.read()
        chk_list = case_idgen_r.split('\n') 
        for no in chk_list:
            if no :
                case_id_gen_cnt+=1
            else:
                case_id_gen.close()
        return case_id_gen_cnt
 
    import os
    chk_file_exist=os.path.exists('Active_patient.txt')
    if os.path.exists('Active_patient.txt'):
        pat_status_serch_active = open('Active_patient.txt','r')
        search_cnt=0

        for lines in pat_status_serch_active:
            lines = lines.rstrip()
            if not pat_id in lines:
                search_cnt+=1
            else:
                break
        pat_status_serch_active.close()

        pat_status_ovrwrite_active_r = open('Active_patient.txt', 'r')
        lists = pat_status_ovrwrite_active_r.readlines()
        pat_status_ovrwrite_active_r.close()

        try:
            del lists[search_cnt]
            pat_status_ovrwrite_active = open('Active_patient.txt', 'w+')
            for line in lists:
                pat_status_ovrwrite_active.write(line)
            pat_status_ovrwrite_active.close()
        except:
            pass
  
        

    if os.path.exists('Deceased_patient.txt') :
        pat_status_serch_dead = open('Deceased_patient.txt','r')
        search_cnt=0

        for lines in pat_status_serch_dead:
            lines = lines.rstrip()
            if not pat_id in lines:
                search_cnt+=1
            else:
                break
        pat_status_serch_dead.close()

        pat_status_ovrwrite_dead_r = open('Deceased_patient.txt', 'r')
        lists = pat_status_ovrwrite_dead_r.readlines()
        pat_status_ovrwrite_dead_r.close()
        try:
            del lists[search_cnt]
            pat_status_ovrwrite_dead = open('Deceased_patient.txt', 'w+')
            for line in lists:
                pat_status_ovrwrite_dead.write(line)
            pat_status_ovrwrite_dead.close()
        except:
            pass 



        pat_status_ovrwrite_dead_r = open('Deceased_patient.txt', 'r')

        lists = pat_status_ovrwrite_dead_r.readlines()
        pat_status_ovrwrite_dead_r.close()
        try:
            del lists[search_cnt]
            pat_status_ovrwrite_dead = open('Deceased_patient.txt', 'w+')
            for line in lists:
                pat_status_ovrwrite_dead.write(line)
            pat_status_ovrwrite_dead.close()
        except:
            pass 
    
    case_id= ''.join(['R',str(case_id_gen())])
    pat_status_active = open('Recovered_patient.txt','a')       
    pat_status_active.write('\n'+case_id+'\t'+pat_id+'\t')
    print('\n\nPatient ID ',pat_id,' (',case_id,') has changed status to "RECOVERED".')
    pat_status_active.close()

#------------------------------------------------------------------------------------------------------
def pat_status_deceased():
    def case_id_gen(): #auto increment id
        case_id_gen =open ('case_id_dead_gen.txt','a')
        case_id_gen.write('\na')
        case_id_gen.close()

        case_id_gen_cnt=0
        case_id_gen2=open('case_id_dead_gen.txt','r')
        case_idgen_r= case_id_gen2.read()
        chk_list = case_idgen_r.split('\n') 
        for no in chk_list:
            if no :
                case_id_gen_cnt+=1
            else:
                case_id_gen.close()
        return case_id_gen_cnt
    
    pat_id =input ('Enter Patient ID: ')
    import os
    if os.path.exists('Active_patient.txt'):
        pat_status_serch_active = open('Active_patient.txt','r')
        search_cnt=0

        for lines in pat_status_serch_active:
            lines = lines.rstrip()
            if not pat_id in lines:
                search_cnt+=1
            else:
                break
        pat_status_serch_active.close()

        pat_status_ovrwrite_active_r = open('Active_patient.txt', 'r')
        lists = pat_status_ovrwrite_active_r.readlines()
        pat_status_ovrwrite_active_r.close()

        try:
            del lists[search_cnt]
            pat_status_ovrwrite_active = open('Active_patient.txt', 'w+')
            for line in lists:
                pat_status_ovrwrite_active.write(line)
            pat_status_ovrwrite_active.close()

        except:
            pass


    
    if os.path.exists('Recovered_patient.txt')  :
        pat_status_serch_recover = open('Recovered_patient.txt','r')
        search_cnt=0

        for lines in pat_status_serch_recover:
            lines = lines.rstrip()
            if not pat_id in lines:
                search_cnt+=1
            else:
                break
        pat_status_serch_recover.close()

        pat_status_ovrwrite_recover_r = open('Recovered_patient.txt', 'r')
        lists = pat_status_ovrwrite_recover_r.readlines()
        pat_status_ovrwrite_recover_r.close()

        try:
            del lists[search_cnt]
            pat_status_ovrwrite_recover = open('Recovered_patient.txt', 'w+')
            for line in lists:
                pat_status_ovrwrite_recover.write(line)
            pat_status_ovrwrite_recover.close()

        except:
            pass 

    case_id=  ''.join(['D',str(case_id_gen())])    
    pat_status_deceased = open('Deceased_patient.txt','a')       
    pat_status_deceased.write('\n'+case_id+'\t'+pat_id)
    print('\nPatient ID ',pat_id,' (',case_id,') has changed status to "DECEASED".\n')
    pat_status_deceased.close()

def pat_status_active_gen(pat_id):
    def case_id_gen(): 
        case_id_gen =open ('case_id_atv_gen.txt','a')
        case_id_gen.write('\na')
        case_id_gen.close()

        case_id_gen_cnt=0
        case_id_gen2=open('case_id_atv_gen.txt','r')
        case_idgen_r= case_id_gen2.read()
        chk_list = case_idgen_r.split('\n') 
        for no in chk_list:
            if no :
                case_id_gen_cnt+=1
            else:
                case_id_gen.close()
        return case_id_gen_cnt

    import os
    if os.path.exists('Recovered_patient.txt'):
        pat_status_serch_recover = open('Recovered_patient.txt','r')
        search_cnt=0

        for lines in pat_status_serch_recover:
            lines = lines.rstrip()
            if not pat_id in lines:
                search_cnt+=1
            else:
                break
        pat_status_serch_recover.close()

        pat_status_ovrwrite_recover_r = open('Recovered_patient.txt', 'r')
        lists = pat_status_ovrwrite_recover_r.readlines()
        pat_status_ovrwrite_recover_r.close()

        try:
            del lists[search_cnt]
            pat_status_ovrwrite_recover = open('Recovered_patient.txt', 'w+')
            for line in lists:
                pat_status_ovrwrite_recover.write(line)
            pat_status_ovrwrite_recover.close()

        except:
            pass 

     
    if os.path.exists('Deceased_patient.txt'):
        pat_status_serch_dead = open('Deceased_patient.txt','r')
        search_cnt=0

        for lines in pat_status_serch_dead:
            lines = lines.rstrip()
            if not pat_id in lines:
                search_cnt+=1
            else:
                break
        pat_status_serch_dead.close()

        pat_status_ovrwrite_dead_r = open('Deceased_patient.txt', 'r')
        lists = pat_status_ovrwrite_dead_r.readlines()
        pat_status_ovrwrite_dead_r.close()

        try:
            del lists[search_cnt]
            pat_status_ovrwrite_dead = open('Deceased_patient.txt', 'w+')
            for line in lists:
                pat_status_ovrwrite_dead.write(line)
            pat_status_ovrwrite_dead.close()

        except:
            pass 

    case_id= ''.join(['A',str(case_id_gen())])
    pat_status_active = open('Active_patient.txt','a')       
    pat_status_active.write('\n'+case_id+'\t'+pat_id+'\t')
    print('\n\nPatient ID ',pat_id,' (',case_id,') has changed status to "ACTIVE".')
    pat_status_active.close()


#----------------------------------quick glance---------------------------------------------------------------------------------------------

def ttl_p_quic_glance_test():    
    try:
        t1n = open ('Test1_negative.txt','r')
        t1n_cnt = 0
        t1n_r = t1n.read()  
        chk_list = t1n_r.split('\n') 
        for no in chk_list:
            if no :
                t1n_cnt+=1
        t1n.close()
    except:
     t1n_cnt = 0
    try:
        t1p = open ('Test1_positive.txt','r')
        t1p_cnt = 0
        t1p_r = t1p.read()
        chk_list = t1p_r.split('\n') 
        for no in chk_list:
            if no :
                t1p_cnt+=1
        t1p.close()
    except:
        t1p_cnt = 0
    t1_total = t1p_cnt+t1n_cnt
    

    try:
        t2n = open ('Test2_negative.txt','r')
        t2n_cnt = 0
        t2n_r = t2n.read()
        chk_list = t2n_r.split('\n') 
        for no in chk_list:
            if no :
                t2n_cnt+=1
        t2n.close()
    except:
        t2n_cnt = 0

    try:
        t2p = open ('Test2_positive.txt','r')
        t2p_cnt = 0
        t2p_r = t2p.read()
        chk_list = t2p_r.split('\n') 
        for no in chk_list:
            if no :
                t2p_cnt+=1
        t2p.close()
    except:
        t2p_cnt=0
        

    t2_total = t2p_cnt+t2n_cnt
    
    try:
        t3n = open ('Test3_negative.txt','r')
        t3n_cnt = 0
        t3n_r = t3n.read()
        chk_list = t3n_r.split('\n') 
        for no in chk_list:
            if no :
                t3n_cnt+=1
        t3n.close()
    except:
        t3n_cnt=0

        
    try:
        t3p = open ('Test3_positive.txt','r')
        t3p_cnt = 0
        t3p_r = t3p.read()
        chk_list = t3p_r.split('\n') 
        for no in chk_list:
            if no :
                t3p_cnt+=1
        t3p.close()
    except:
        t3p_cnt=0
        

    t3_total = t3p_cnt+t3n_cnt

#------------------------------------------------------------------------------------
    
        
    try:
        chk_active = open('Test1_positive.txt','r')
        chk_ato = 'ATO'
        t1_ato_cnt=0
        for line in chk_active:
            line=line.rstrip()
            if  chk_ato in line:
                t1_ato_cnt+=1
            else:
                continue
        else:
            chk_active.close()
        
    except:
        t1_ato_cnt=0

    try:
        chk_active = open('Test1_positive.txt','r')
        chk_acc = 'ACC'
        t1_acc_cnt=0
        for line in chk_active:
            line=line.rstrip()
            if  chk_acc in line:
                t1_acc_cnt+=1
            else:
                continue
        else:
            chk_active.close()
    except:
        t1_acc_cnt=0

    try:
        chk_active = open('Test1_positive.txt','r')
        chk_aeo = 'AEO'
        t1_aeo_cnt=0
        for line in chk_active:
            line=line.rstrip()
            if  chk_aeo in line:
                t1_aeo_cnt+=1
            else:
                continue
        else:
            chk_active.close()
    except:
        t1_aeo_cnt=0




    try:
        chk_active = open('Test1_positive.txt','r')
        chk_sid = 'SID'
        t1_sid_cnt=0
        for line in chk_active:
            line=line.rstrip()
            if  chk_sid in line:
                t1_sid_cnt+=1
            else:
                continue
        else:
            chk_active.close()
    except:
        t1_sid_cnt=0

    try:
        chk_active = open('Test1_positive.txt','r')
        chk_ahs = 'AHS'
        t1_ahs_cnt=0
        for line in chk_active:
            line=line.rstrip()
            if  chk_ahs in line:
                t1_ahs_cnt+=1
            else:
                continue
        else:
            chk_active.close()
    except:
        t1_ahs_cnt=0

#=================================================================================================================================
      
    try:
        chk_active = open('Test2_positive.txt','r')
        chk_ato = 'ATO'
        t2_ato_cnt=0
        for line in chk_active:
            line=line.rstrip()
            if  chk_ato in line:
                t2_ato_cnt+=1
            else:
                continue
        else:
            chk_active.close()
        
    except:
        t2_ato_cnt=0

    try:
        chk_active = open('Test2_positive.txt','r')
        chk_acc = 'ACC'
        t2_acc_cnt=0
        for line in chk_active:
            line=line.rstrip()
            if  chk_acc in line:
                t2_acc_cnt+=1
            else:
                continue
        else:
            chk_active.close()
    except:
        t2_acc_cnt=0

    try:
        chk_active = open('Test2_positive.txt','r')
        chk_aeo = 'AEO'
        t2_aeo_cnt=0
        for line in chk_active:
            line=line.rstrip()
            if  chk_aeo in line:
                t2_aeo_cnt+=1
            else:
                continue
        else:
            chk_active.close()
    except:
        t2_aeo_cnt=0



    try:
        chk_active = open('Test2_positive.txt','r')
        chk_sid = 'SID'
        t2_sid_cnt=0
        for line in chk_active:
            line=line.rstrip()
            if  chk_sid in line:
                t2_sid_cnt+=1
            else:
                continue
        else:
            chk_active.close()
    except:
        t2_sid_cnt=0

    try:
        chk_active = open('Test2_positive.txt','r')
        chk_ahs = 'AHS'
        t2_ahs_cnt=0
        for line in chk_active:
            line=line.rstrip()
            if  chk_ahs in line:
                t2_ahs_cnt+=1
            else:
                continue
        else:
            chk_active.close()
    except:
        t2_ahs_cnt=0
#=======================================================================================================================================
      
    try:
        chk_active = open('Test3_positive.txt','r')
        chk_ato = 'ATO'
        t3_ato_cnt=0
        for line in chk_active:
            line=line.rstrip()
            if  chk_ato in line:
                t3_ato_cnt+=1
            else:
                continue
        else:
            chk_active.close()
        
    except:
        t3_ato_cnt=0

    try:
        chk_active = open('Test3_positive.txt','r')
        chk_acc = 'ACC'
        t3_acc_cnt=0
        for line in chk_active:
            line=line.rstrip()
            if  chk_acc in line:
                t3_acc_cnt+=1
            else:
                continue
        else:
            chk_active.close()
    except:
        t3_acc_cnt=0

    try:
        chk_active = open('Test3_positive.txt','r')
        chk_aeo = 'AEO'
        t3_aeo_cnt=0
        for line in chk_active:
            line=line.rstrip()
            if  chk_aeo in line:
                t3_aeo_cnt+=1
            else:
                continue
        else:
            chk_active.close()
    except:
        t3_aeo_cnt=0




    try:
        chk_active = open('Test3_positive.txt','r')
        chk_sid = 'SID'
        t3_sid_cnt=0
        for line in chk_active:
            line=line.rstrip()
            if  chk_sid in line:
               t3_sid_cnt+=1
            else:
                continue
        else:
            chk_active.close()
    except:
        t3_sid_cnt=0

    try:
        chk_active = open('Test3_positive.txt','r')
        chk_ahs = 'AHS'
        t3_ahs_cnt=0
        for line in chk_active:
            line=line.rstrip()
            if  chk_ahs in line:
                t3_ahs_cnt+=1
            else:
                continue
        else:
            chk_active.close()
    except:
        t3_ahs_cnt=0

#------------------------------------------------------------------------------------------------------------------------------------------
#test1
    try:
        chk_active = open('Test1_positive.txt','r')
        chk_zonA = '!'
        t1_zonA_cnt=0
        for line in chk_active:
            line=line.rstrip()
            if  chk_zonA in line:
                t1_zonA_cnt+=1
            else:
                continue
        else:
            chk_active.close()
    except:
        t1_zonA_cnt=0

    try:
        chk_active = open('Test1_positive.txt','r')
        chk_zonB = '@'
        t1_zonB_cnt=0
        for line in chk_active:
            line=line.rstrip()
            if  chk_zonB in line:
                t1_zonB_cnt+=1
            else:
                continue
        else:
            chk_active.close()
    except:
        t1_zonB_cnt=0

    try:
        chk_active = open('Test1_positive.txt','r')
        chk_zonC = '#'
        t1_zonC_cnt=0
        for line in chk_active:
            line=line.rstrip()
            if  chk_zonC in line:
                t1_zonC_cnt+=1
            else:
                continue
        else:
            chk_active.close()
    except:
        t1_zonC_cnt=0

    try:
        chk_active = open('Test1_positive.txt','r')
        chk_zonD = '$'
        t1_zonD_cnt=0
        for line in chk_active:
            line=line.rstrip()
            if  chk_zonD in line:
                t1_zonD_cnt+=1
            else:
                continue
        else:
            chk_active.close()
    except:
        t1_zonD_cnt=0
#--------------------------test2
    try:
        chk_active = open('Test2_positive.txt','r')
        chk_zonA = '!'
        t2_zonA_cnt=0
        for line in chk_active:
            line=line.rstrip()
            if  chk_zonA in line:
                t2_zonA_cnt+=1
            else:
                continue
        else:
            chk_active.close()
    except:
        t2_zonA_cnt=0

    try:
        chk_active = open('Test2_positive.txt','r')
        chk_zonB = '@'
        t2_zonB_cnt=0
        for line in chk_active:
            line=line.rstrip()
            if  chk_zonB in line:
                t2_zonB_cnt+=1
            else:
                continue
        else:
            chk_active.close()
    except:
        t2_zonB_cnt=0

    try:
        chk_active = open('Test2_positive.txt','r')
        chk_zonC = '#'
        t2_zonC_cnt=0
        for line in chk_active:
            line=line.rstrip()
            if  chk_zonC in line:
                t2_zonC_cnt+=1
            else:
                continue
        else:
            chk_active.close()
    except:
        t2_zonC_cnt=0

    try:
        chk_active = open('Test2_positive.txt','r')
        chk_zonD = '$'
        t2_zonD_cnt=0
        for line in chk_active:
            line=line.rstrip()
            if  chk_zonD in line:
                t2_zonD_cnt+=1
            else:
                continue
        else:
            chk_active.close()
    except:
        t2_zonD_cnt=0
#--------------------- test 3
    try:
        chk_active = open('Test3_positive.txt','r')
        chk_zonA = '!'
        t3_zonA_cnt=0
        for line in chk_active:
            line=line.rstrip()
            if  chk_zonA in line:
                t3_zonA_cnt+=1
            else:
                continue
        else:
            chk_active.close()
    except:
        t3_zonA_cnt=0

    try:
        chk_active = open('Test3_positive.txt','r')
        chk_zonB = '@'
        t3_zonB_cnt=0
        for line in chk_active:
            line=line.rstrip()
            if  chk_zonB in line:
                t3_zonB_cnt+=1
            else:
                continue
        else:
            chk_active.close()
    except:
        t3_zonB_cnt=0

    try:
        chk_active = open('Test3_positive.txt','r')
        chk_zonC = '#'
        t3_zonC_cnt=0
        for line in chk_active:
            line=line.rstrip()
            if  chk_zonC in line:
                t3_zonC_cnt+=1
            else:
                continue
        else:
            chk_active.close()
    except:
        t3_zonC_cnt=0

    try:
        chk_active = open('Test3_positive.txt','r')
        chk_zonD = '$'
        t3_zonD_cnt=0
        for line in chk_active:
            line=line.rstrip()
            if  chk_zonD in line:
                t3_zonD_cnt+=1
            else:
                continue
        else:
            chk_active.close()
    except:
        t3_zonD_cnt=0
#--------------------------------------------

    ttl_zonA= t1_zonA_cnt+t2_zonA_cnt+t3_zonA_cnt
    ttl_zonB= t1_zonB_cnt+t2_zonB_cnt+t3_zonB_cnt
    ttl_zonC= t1_zonC_cnt+t2_zonC_cnt+t3_zonC_cnt
    ttl_zonD= t1_zonD_cnt+t2_zonD_cnt+t3_zonD_cnt
    ttl_pat_tested = t1_total + t2_total + t3_total
    ttl_ato = t1_ato_cnt+t2_ato_cnt+t3_ato_cnt
    ttl_acc = t1_acc_cnt+t2_acc_cnt+t3_acc_cnt
    ttl_aeo = t1_aeo_cnt+t2_aeo_cnt+t3_aeo_cnt
    ttl_sid = t1_sid_cnt+t2_sid_cnt+t3_sid_cnt
    ttl_ahs = t1_ahs_cnt+t2_ahs_cnt+t3_ahs_cnt
    ttl_t1_positive =t1_ato_cnt+t1_acc_cnt+t1_aeo_cnt+ t1_sid_cnt+t1_ahs_cnt
    ttl_t2_positive =t2_ato_cnt+t2_acc_cnt+t1_aeo_cnt+ t2_sid_cnt+t2_ahs_cnt
    ttl_t3_positive =t3_ato_cnt+t3_acc_cnt+t3_aeo_cnt+ t3_sid_cnt+t3_ahs_cnt
    ttl_positive = ttl_t1_positive + ttl_t2_positive + ttl_t3_positive
    
    try:
        t1_positive_rates = (ttl_t1_positive/t1_total)*100
    except:
        t1_positive_rates=0
    try:
        t2_positive_rates = (ttl_t2_positive/t2_total)*100
    except:
        t2_positive_rates=0
    try:
        t3_positive_rates = (ttl_t3_positive/t3_total)*100
    except:
        t3_positive_rates=0
    try:
        ttl_positive_rates = (ttl_positive/ttl_pat_tested)*100
    except:
        ttl_positive_rates = 0
    
    print('\nTest:\t|\tPatient tested:\t|\tTotal Test Positive Zone:\t|\tTotal Test Positive group:\t\t|  Test Positive Ratio:')
    print('\t|\t\t\t|\tA\tB\tC\tD\t|\tATO\tACC\tAEO\tSID\tAHS\t|')
    print('T1:\t|\t',t1_total,'\t\t|\t',t1_zonA_cnt,'\t',t1_zonB_cnt,'\t',t1_zonC_cnt,'\t',t1_zonD_cnt,'\t|\t',t1_ato_cnt,'\t',t1_acc_cnt,'\t',t1_aeo_cnt,'\t',t1_sid_cnt,'\t',t1_ahs_cnt,'\t|\t',round(t1_positive_rates,1),'%')
    print('T2:\t|\t',t2_total,'\t\t|\t',t2_zonA_cnt,'\t',t2_zonB_cnt,'\t',t2_zonC_cnt,'\t',t2_zonD_cnt,'\t|\t',t2_ato_cnt,'\t',t2_acc_cnt,'\t',t2_aeo_cnt,'\t',t2_sid_cnt,'\t',t2_ahs_cnt,'\t|\t',round(t2_positive_rates,1),'%')
    print('T3:\t|\t',t3_total,'\t\t|\t',t3_zonA_cnt,'\t',t3_zonB_cnt,'\t',t3_zonC_cnt,'\t',t3_zonD_cnt,'\t|\t',t3_ato_cnt,'\t',t3_acc_cnt,'\t',t3_aeo_cnt,'\t',t3_sid_cnt,'\t',t3_ahs_cnt,'\t|\t',round(t3_positive_rates,1),'%')
    print('Total:\t|\t',ttl_pat_tested,'\t\t|\t',ttl_zonA,'\t',ttl_zonB,'\t',ttl_zonC,'\t',ttl_zonD,'\t|\t',ttl_ato,'\t',ttl_acc,'\t',ttl_aeo,'\t',ttl_sid,'\t',ttl_ahs,'\t|\t',round(ttl_positive_rates,1),'%')



def ttl_AnRnD_quic_glance():
    def ttl_counter():
        
        try:
            atv_pat = open('Active_patient.txt','r')
            atv_pat_cnt= 0
            atv_pat_r =atv_pat.read()
            chk_list = atv_pat_r.split('\n')
            for no in chk_list:
                if no :
                    atv_pat_cnt+=1
            atv_pat.close()
        except:
            atv_pat_cnt=0       

        try:
            rec_pat = open('Recovered_patient.txt','r')
            rec_pat_cnt= 0
            rec_pat_r =rec_pat.read()
            chk_list = rec_pat_r.split('\n')
            for no in chk_list:
                if no :
                    rec_pat_cnt+=1
            rec_pat.close()
        except:
            rec_pat_cnt=0       
  
        try:
            dead_pat = open('Deceased_patient.txt','r')
            dead_pat_cnt= 0
            dead_pat_r =dead_pat.read()
            chk_list = dead_pat_r.split('\n')
            for no in chk_list:
                if no :
                    dead_pat_cnt+=1
            dead_pat.close()
        except:
            dead_pat_cnt=0    
        avg_recover_rate = rec_pat_cnt/(atv_pat_cnt+rec_pat_cnt+dead_pat_cnt)
        recover_rate= ''.join([str(round(avg_recover_rate*100,1)),'%'])

        print(atv_pat_cnt,'\t',rec_pat_cnt,'\t\t',dead_pat_cnt,'\t\t',recover_rate,'\n')
    print('\nActive\tRecovered\tDeceased\tRecovery Rate')
    try:
        ttl_counter()
    except:
        print('0\t0\t\t0\t\t0.0%\n')

#==============================    search         =============================================================================================

def patient_detail_search():
    import os
    pat_id = input ('Enter patient id or name: ')
    if os.path.exists('Patient_id.txt'):
        pat_search= open('Patient_id.txt','r')
        for line in pat_search:
            line = line.rstrip()
            if not pat_id in line:
                continue
            else:
                print('PatientID\tName\tGender\tBlood type\tPhone Number\tZone\tGroup Code')
                print (line)
                break
        else:
            print('\n',pat_id,'not founded in the patient ID database')
    else:
        print('\n',pat_id,'not founded in the patient ID database')

#----------------------------------------------------------------------------------------------
def test_search():
    pat_id = input ('Enter Patient ID: ')
    flag =0
    try:
        pat_test_serch_active = open('Test1_negative.txt','r')
        for lines in pat_test_serch_active:
            lines = lines.rstrip()
            if not pat_id in lines:
                continue
            else:
                flag=1
                print('Test\t\tPatient ID\tAction take\tHospitalization')
                print ('T1 NEGATIVE',lines)    
                break
        pat_test_serch_active.close()
    except:
        pass

    try:
        pat_test_serch_active = open('Test2_negative.txt','r')
        for lines in pat_test_serch_active:
            lines = lines.rstrip()
            if not pat_id in lines:
                continue
            else:
                flag=1
                print ('\nT2 NEGATIVE\t',lines)    
                break
        pat_test_serch_active.close()
    except:
        pass

    try:
        pat_test_serch_active = open('Test3_negative.txt','r')
        for lines in pat_test_serch_active:
            lines = lines.rstrip()
            if not pat_id in lines:
                continue
            else:
                flag=1
                print ('\nT3 NEGATIVE\t',lines)    
                break
        pat_test_serch_active.close()
    except:
        pass

    try:
        pat_test_serch_active = open('Test1_positive.txt','r')
        for lines in pat_test_serch_active:
            lines = lines.rstrip()
            if not pat_id in lines:
                continue
            else:
                flag=1
                print('Test\t\tPatient ID\tAction take\tHospitalization')
                print ('T1 POSITIVE\t',lines)    
                break
        pat_test_serch_active.close()
    except:
        pass

    try:
        pat_test_serch_active = open('Test2_positive.txt','r')
        for lines in pat_test_serch_active:
            lines = lines.rstrip()
            if not pat_id in lines:
                continue
            else:
                flag=1
                print ('\nT2 POSITIVE\t',lines)    
                break
        pat_test_serch_active.close()
    except:
        pass

    try:
        pat_test_serch_active = open('Test3_positive.txt','r')
        for lines in pat_test_serch_active:
            lines = lines.rstrip()
            if not pat_id in lines:
                continue
            else:
                flag=1
                print ('\nT3 POSITIVE\t',lines)    
                break
        pat_test_serch_active.close()
    except:
        pass

    if(flag==0):
        print(pat_id,'not found or not yet recorded in T1,T2,T3 Database.')

#---------------------------------------------------------------------------------------------------

def case_search():
    flag=0
    pat_id = input ('Enter case ID: ')
    print('\nCase ID\tPatient ID\tPatient Status')
    try:
        pat_search= open('Active_patient.txt','r')
        for line in pat_search:
            line = line.rstrip()
            if not pat_id in line:
                continue
            else:
                print (line,'\t\tACTIVE')
                flag=1
                break
                
    except:
        pass

    try:
        pat_search= open('Recovered_patient.txt','r')
        for line in pat_search:
            line = line.rstrip()
            if not pat_id in line:
                continue
            else:
                print (line,'\t\tRECOVERED')
                flag=1
                break
                
    except:
        pass
    
    try:
        pat_search= open('Deceased_patient.txt','r')
        for line in pat_search:
            line = line.rstrip()
            if not pat_id in line:
                continue
            else:
                print (line,'\t\tDECEASED')
                flag=1
                break
    except:
        pass
    if (flag!=1 or pat_id ==''): 
        print('n/a\tn/a\t\tn/a')
        print('\n\nCase ID ',pat_id,' not yet recorded in the patient status database.\n')


















#++++++++++++++++++++++++++++++++++++++++++++++++++++++++interface option++++++++++++++++++++++++++++++++++++++++++++++++++++++





def pat_status():
    loop = 'y'
    while (loop =='y'):
        print('\n1. Create or Change Patient Status \n2. Patient Status Overview \n3. Case Search \n0. Back')
        pat_status_opt= input('Patient Status / Enter Your Option from 1 to 0 : ')
        if(pat_status_opt=='1'):
           print('1. Active \n2.Recovered \n3. Deceased\n0. Back')
           pat_status_opt_c= input('Create or Change Patient Status / Enter your option from 1 to 0: ')
           if (pat_status_opt_c=='1'):
               pat_status_active()
           elif(pat_status_opt_c=='2'):
               pat_status_recovered()
           elif(pat_status_opt_c=='3'):
               pat_status_deceased()
        elif(pat_status_opt=='2'):
            ttl_AnRnD_quic_glance()
        elif(pat_status_opt=='3'):
            case_search()
        elif(pat_status_opt=='0'):
            break
  




def tes_opt():
    loop = 'y'
    while(loop=='y'):
        print('\n\n1. File new test record \n2. Test Record Overview \n3. Patient Search in Test \n0. Back')
        tes_opt = str(input('Test Reslt& Action / Enter option from 1 to 0 :'))
        if(tes_opt=='1'):
           
            print('\n\n1. Test 1 \n2. Test 2 \n3. Test 3 \n0.Back')
            tes_opt = str(input('New Record / Enter option from 1 to 0 :'))
            if(tes_opt=='1'):
                new_tes_rec1()
            elif(tes_opt=='2'):
                new_tes_chk_rec2()
            elif(tes_opt=='3'):
                new_tes_chk_rec3()
        
        elif(tes_opt=='2'):
            ttl_p_quic_glance_test()
        
        elif(tes_opt=='3'):
            test_search()

        elif(tes_opt=='0'):
            break
                

        else:
            continue      
    






print('Covid-19 Patient Management System [FSD2002-1F] \n(c) 2020 Yap Seng Long (TP-060075). All rights reserved.\n\n')
choice = str(input('Enter any key to continue or enter x to exit: '))
while(choice!='x'):
    print('\n1. New Patient Registration \n2. Test Results and Action Taken \n3. Setting and Changing Patient Status \n4. Patient ID Search \n0. Exit')
    main_opt = str (input('Enter Your option from 1 to 0:'))
    if (main_opt=='1'):
        patient_detail()

    elif(main_opt=='2'):
        tes_opt()
    elif(main_opt=='3'):
        pat_status()
    elif(main_opt=='4'):
        patient_detail_search()

    elif(main_opt=='0'):
        break
    else:
        continue
