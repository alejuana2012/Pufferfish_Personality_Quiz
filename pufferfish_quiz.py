from pathlib import Path
import numpy

#Paths to the folder where the project is and where we want to write the certificate text file
path_to_project = Path("D:\LU//22-23\Winter\CMSC140\Final_Project")
project_dir = path_to_project / "pufferfish_quiz.py"
out = project_dir / "certificate.txt"

#A list containing beautiful ASCII pufferfish that will be printed under the header of the certificate text tile. (Made using https://manytools.org/hacker-tools/convert-images-to-ascii-art/)
puffers =[
    '''                                                                                                    
                                           @    @   @   @                                           
                               @   @@@.     @          @@    @@@@@@@ @@                             
                             @@.@@                                    @                             
                          @@                                            .@@                         
                        @                                                  @@                       
                       @                                                     @                      
             @@@@     @            @@@@@@@@               @@@@@@@@            @@    @@@@            
            @      @@@            @@@@@    @@            @@   @@@@@@           @@@      @           
          @@          @           @@@@@@@@@@@   @@@@@   .@@@@@@@@@@@          @          @@         
           @@%@                    @@@@@@@@     @@@@@     @@@@@@@@@                    %@@          
            @.     @@.                           @@@@                           @@      @           
              @@,  @@                                                            @  *@@             
                    @                                                           @/                  
                    @@                                                          @                   
                     @@                                                        @                    
                       @                                                     @@                     
                        @@           @@                      @@@           @@                       
                           @@@@      @, @@                 @   @     @@@ @@                         
                           @@  @@                                  @@  @@                           
                                 @@@ @@                       @@ @@@                                
                                    .@  @@@@@    @@ @@  %@@@@  @@                                   
                                                 @@  @ 
    ''',
    '''                                                                                                   
                                                                  %                                 
                              (                 .#               %%                                 
                              *%#               %%%            %%%(                                 
                               %%%% %%         %(/%%         .%(/%                                  
                                %(/%%%%%%%%%%%#/////%##%%%%%%///(%                                  
                                ,%//##//(%#///////////%#%%///////%%%           %                    
              %%.           .%%%/%//%///////////////(%///%(//////////%%%.  /%#%                     
                %%#%%*   /%%(/////////////////////////////%////////////((((((%,                     
                  %%///(%%%(///////////////////////////////////////(/////((((%                      
                    %#///////////////////////////////////////%%%#((((#%%%(((((%%          .#%.      
                   %%/(////////////////////////////////////%%((((((((((((#%/((((%%/%%%%##%,         
                 #%(/////////#%%#((((#%%#/////////////////%((((((((((((((((%(((((((((%%/            
                %%/////////(%((((((((((((%(//////////////#((((((((((((((((((%((((((%%               
               %%(###(/////((((((((((((((((//////////////((((           ((((((((((((%%              
  /%%%%%%%%%#(///(%///////(((((       .(((((/////////////((.              %(((((((((#%%             
   %%%*  /%%#///////(///////%         &%,((////////////////  /  @@        .%((((((((((((%%    (%%%  
  %%((((%%%( %%%//////////#%%%%%(  *#&&& ((////////////////  &(&&& .#%%%%%%%((/(((((##%% %%%#((((%# 
 %%/((((((((%%(////////////((/(((((#%&&/*/////////////////// .&&%%((///(((((((((((((((#%#(((((((((%(
 %(/((((#%%%%%////////////////((/((((((#//////////////////////(/(///////////(((((((((((((##%%%((//%%
 %%/(((((((((%//((/////////////(/((((((((#/////////////////(/////////////////(((((((((((%(((((((//%%
 %%//((#%%%%%%(/////////////////(/((((((((##//////////////%////////////*/////((((((((((%%%%#(((///%%
 %%(((((((%%%%%(////////////////(/(((((((((%%///////////(%(//////////////////(((((((((#%%%%(((((((%%
  ,%(((((%%%#/(%///////////////(((((((((((((%%%%%%##%%%%%#((/////////////////((((((((#%((%%%((((#%  
   %%%%,   %#((//////////////(((((((((((((((%///////////%#(((//////////////((((((((((((((%,  *%%%%  
           %%((/((////////(((((((((((((((((%(////////////%((((((////////((((((((((((((((%%          
            %%%/((((((((((((((((((((((((((#///////////////%((((((((((((((((((((((((((((%%           
             %#((((((((((((((((((((((((((///////////////////(((((((((((((((((((((((((((%%           
            %%%%%((((((((((((((((((((((////////////////////(((((((((((((((((((((((((%%,%%%          
                 /%%#((%((((((((((((/////////////////(((((((((((((((((((((((((((#%%#                
                     .%%%%%#/(((((((///////((/((((((((((#((((((((((((((((#%%%%%(%                   
                      ,, *%(((%((((((((((((((((((((((((((((((((((((((((((#%,    %                   
                         %#(%%%(((((((((((((((((((((((((((((((#((((%(%#(((%                         
                        (%%% .%((#%%%(((((((((((((((((((%(((((%%(((%    %%%#                        
                        %%   %%%      .%#((%(((((#(##%%%%%%#((% .%%%        (                       
                       %     ,         ,%((#%((%.          ,%(%*   #.                               
                                        %(%%%%%              (%%                                    
                                        %#%  %                 %(                                   
                                        #%                                                          
                                        *.     
    ''',
    '''                                                                                                                                                                                                                                                                                                        
                                             *&@@@&@@@#,                                            
                                       ,@&####*********####@@                                       
          *#%%/                    (@@@@&#########(#########&@@@@,                   .(&%(.         
      *@    ,@    @(            ,@*#. ***@#################@**. #.%@             &@   .@     @      
     @ .       /&   ./@       *@@,#*@(//@##################%%*/&&,@ @@        @..   @.       , @    
    % *@.  .      @* .  &.   @#%*     @%#####################&%     @##@   %#  . %#      ,  *@  @   
   &  .   (@  ,     .@    (/@#####&%###########(((((#############%&#####@&,   .@      . .@,     ,*  
   %      .   @.    .. &/ .&#########(*.        &@@@#        ,/##########@  &( .     %@   .     /,  
    @  .         %#     ./@####(,           @(*/(/(((/*%&          .*(####@ ,.    &(        .   @   
    .& @@*          #&.@&@(*.            (&(//@%(/(((@&/((@.            .*#@@#.@.          (@# @    
      @ .   *@#     @%%#&              .@((&#((((###((((&%((@               @(#&%     %&..  . @     
        @      . &@.                   (@@*@@@*.*///, %@@@&@@                    /@*       ,@       
          .@/  %/                                                                   %,  #&          
             .&.                                                                      @             
            @                                                                          ,%           
           &                            .#%%    .    #%%.                                @          
          @                              %%##        %%#                                  @         
         @                                %%%#      .%%%                                   @        
        &                                  #%#.      #%#.                                  ,*       
        %        .                         %%%/      ,%%%/                         .        @       
       &                                  %%%%         (#%%%%%%*                            **      
       @                               #%#%#.               *%%%%%#%%#%%                     @      
       @                           *%%%%%/                          .*/.                     @      
       @                        /%#%%#        .%%%%%%###%(                                   @      
       @                                    ###%%.    .#%%%%%*                .              &      
       #.                                ,%%%%(            ##%%#%%                          #       
        @     .                        #%%##                   (%#                    .     @       
         @                            %%%/     .     ,                                     @        
          @                                                                             ..&         
           /(.                                                                          @           
             /&                                                                      .@.            
                @#//,                                                           */*@%               
                   .@(***//*.                                           .*/*/**%&                   
                        #@#/**/*******/*,.                 .,*********/*/*&@*                       
                              ./&@&#/***************************/#@@%*                              
                                            ,/##&##%&##/,                                           
                                                                                                   
    ''',
    '''
                                                            ((                                          
                                            /          (((,      ((.         (((                    
                                ((          (((*((((((((((((((((((((((((( ((((((                    
                                 ((((   /((((((((((((((#(((((((((/#((((((((((((((                   
                           *      ((((((((((((/#(((((((##(((((((###(((((((((((((((((,               
                            (( ,((((((##((((/((###(((((/(((((((((..((((((((((((((((((((.            
                  .    #(   ((((((((((###(/((((###((((((((((            (((((((((((((((((( .(##     
                        ((((((((((((/(((((((((((((((((((((/       ###### ((((((((((((((((((/###     
                       ((((/(((((((((##(((((((((((((((((((       #######* (((((((((((((((((((       
       %###(((       ((((((###((((((((#####((((((((((((((((        ###%  .((((((((((((((((((((      
      #####(((((    (((((((/###((((((((###((((((##(((((((((/            ((((((((((#.                
     ######((((((  (((((((((((((((((((((((((((((###/(((((((((((.     (((((((((((                    
    *######(((((((((((((((((((((/(((((((((((((((((((((((((((((((((((((((((((((((                 .  
    (######((((((((((((((((((((((##((((((((((((((((((((((((((((((((((((((((((((((* .           ..   
    ,######((((((((((((((((((((((###((((((((((((((((((((((((((((((((((((((((((((((.,,,,,,,,,,,,,    
     ######(((((((((((//(((((((((((((((((((,            .(((((((((((((((/((((((((/..............    
     %#####/(((((((((/((((((((            ...           ((((((((((((/%         ((((.........,,      
      %####%(((((/(  (((           ,,,                 /(#%###########                 ,(((((       
       #####/(((((                 ,,,,       .,,      ##############                               
        %####/(((                          ,            /#######%.                                  
                                 ,                                                                  
                               .,,,,   ,,,      ,,,                                                 
                                                 , 
    ''',
    '''                                                                                                    
                                                                                                    
                                                                                                    
                                                       ,,             ,                             
                                           ,,         ,,,,          ,,,.                            
                                           ,,,       ,,,,,.        ,,,,,                            
                                           ,,,,,    ,,,,,,,      ,,,,,,,                            
                                  ,        ,,,,,,, .,,,,,,,,   ,,,,,,,,,                            
                                  ,,,,     ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,        ,,                  
                                   ,,,,,,  ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,    .,,,,                   
                                   ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,, ,,,,,,,                    
                                   .,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,                    
                                  ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,                  
                              ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,.              
   ***,                    ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,            
     *********           ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,.         
       .**********     ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,        
         *************,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,      
           **********,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,     
           .********,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,       ,,,,,,,,,,    
            ********,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,              ,,,,,,    
            ********,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,           .&&.  ,,,,,    
            ********,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,           *&&&&/  ,,,,    
           **********,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,.                  ,,,,    
          **********  ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,******,,,,,,,,,,,,,,                 ,,,,     
        .*******       ,,,,,,,,,,,,,,,,,,,,,,,,,,,,************,,,,,,,,,,,,,             .,,,,      
       ****,            ,,,,,,,,,,,,,,,,,,,,,,,,,****************,,,,,,,,,,,,,,,     .,,,,,,,//     
                          ,,,,,,,,,,,,,,,,,,,,,********************,,,,,,,,,,,,,,,,,,,,,,,,,////    
                            .,,,,,,,,,,,,,,,,,**********************,,,,,,,,,,,,,,,,,,,,,,/////     
                               .,,,,,,,,,,,,,************************,,,,,,,,,,,,,,,,,,,////        
                                   .,,,,,,,,,************************,,,,,,,,,,,,,,,    /(          
                                         ,,,,************************,,,,,,,,,,                     
                                              **********************                                
                                                ******************                                  
                                                   ***********,                                    
    ''',
    '''                                                                                                                                                                                                    
                .##,                                                                                
              *&,   &(                                                                              
              .&(,.(&.                                                                              
         (&&&.                                                                                      
       (&,   ,&                                                                                     
       /&,...(&                                   (                                                 
          /#*.&&&&&&*                     %&     %&%    .&#      .                                  
            &%.     *&             #&%   (&#&&&&&%#&&&&&&#&/   %&/                                  
            &/.     ,&.      &(    &&#%&&&%###%%#####%%###%&&&%#&&    (&                            
             %&(,,*&&.       (&#&&&&%###########################%&&&&#&/                            
                       ,&&#*#&&######################################%&&#/%&&.                      
     /&&%(%&&&/         (&#################################################&/         /&&&%(%&&*    
   /&/,,,,,,,,,#&&,&&#(&&&&###############################################&&&&(#&&.&&(,,,,,,,,,(&*  
  (&,,,,,,,,,,,,,,%&&&#########################################################&&&%,,,,,,,,,,,,,,&( 
  &/,,,,,,,,,,,,,,,,&&&############(/**/(##################((((###############&&&,,,,,,,,,,,,,,,,(&.
 .&*,,,,,,,,,,,,,,(###########**********,,,,,/#######************,**(############*,,,,,,,,,,,,,,,/&.
  *&&,,,,,,,,,,,(&&&#######/*****.              ##/*****.              #########%&&&/,,,,,,,,,,,&&, 
      .(###(*../&&&&######***,       *%&%/       ***,       .//*        /########&&&&*  *(###(.     
               &&%#######**.     (&&%&&&&&&&&(  **.     /&&&&&&&&&&&.    (#########%&&              
                ,&&%#####,      &&%  ,&&&&&&&&& ,      &&(  *&&&&&&&&&   ,#######%&&,               
             .&&&########      /&&&&&&&&&&&&&&&(      %&&&&&&&&&&&&&&&,  *##########&&&,            
              .&&&%###(***      &&&&&&&&&&&&&&&       *&&&&&&&&&&&&&&&   *****(###%&&%              
                /&&(*******      &&&&&&&&&&&&&  .*     .&&&&&&&&&&&&&   *********(&&,               
              #&#************       %&&&&&%   .*****      /&&&&&&&.  .**************%&#             
                 &&&&************.        ,*************         .**************&&&%.               
                 .&&*************************************************************&&.                
               .&&&&&&(******************(&&&%%&&&&&&&&&&*********************(&&&&&&               
                    .&&********************/&&&&&&&&&&%**********************/&&.                   
                    &#*/(/*************************************************((/*%&                   
                  /.    &&&***********************************************&&&    ./                 
                        #&*(&&&***************************************&&&(*&#                       
                       (%.   &&/*************************************/&&   .%(                      
                             #&&&&&&%***************************%&&&&&&(                            
                             (     &%(&&&&%**/&&#***#&&/**&&&&&/&&     #                            
                                   #&.   .&(&&.*&&*&&,.&&(&.    &/                                  
                                          ((     /&,     #(                                         
                                                                                                    
    '''
]

#The descriptive text of each of the 6 pufferfish personalities. They will be printed to the bottom of the certificate text file upon completion
puffer_bios = [
    '''**You are the PUFFY PUFFERFISH!** 
Traits of this puffer are:
    -outgoing
    -responsible
    -charismatic
This fugu is the main character. Humility runs through their veins, but don't let that fool you! Their skills are immense and their reputation preceeds them.
Honorable describes this fish! They will always take the lead but won't always take the credit.
Their only weakness is that they don't like conflict; if anything they will sugar coat their feelings and ideas''',
    '''**You are the SPIKY PUFFERFISH!** 
Traits of this puffer are:
    -clever
    -sneaky
    -resourceful
This fugu is as confident as they are quippy. They know how cool they are, and aren't afraid to prove it to you.
Action hungry describes this fish! They can talk their way out of sticky situations and will do it with style.
Their only weakness is that their hubris can cloud their judgement, making near-death experiences common.''',
    '''**You are the MENACING PUFFERFISH!** 
Traits of this puffer are:
    -brusque
    -reserved
    -(secretly) loving
This fugu is a force to be reckoned with. They don't care for fancy things or small talk. They work well under pressure.
"Friendly when calm, deadly when angry" describes this fish! If it weren't for the need to correct injustice, this fish wouldn't have a care in the world.
Their only weakness is that they do not get along with everyone. They may seem heartless when in reality their actions reflect how much they care.''',
    '''**You are the SQUISHY PUFFERFISH!** 
Traits of this puffer are:
    -ambitious
    -stylish
    -loyal
This fugu is comfortable in any environment. They know how to make an entrance but are totally chill about it. 
Cool as a cucumber describes this fish! They know how to work with people and are the best at bringing joy to any situation.
Their only weakness is that their fear can get the best of them. But if they can coexist with their intrusive throughts, success is in their hands.''',
'''**You are the ELOQUENT PUFFERFISH!** 
Traits of this puffer are:
    -organized
    -analytical
    -stubborn
This fugu is the talk of the town. They won't tell you how much their outfit cost, but you will always find them making impeccable style choices.  
Beautiful and powerful describes this fish! They have important goals and will do everything in their power to reach those goals.
Their only weakness is that they cannot be persuaded. They will always stick to their moral code and luck tends to be on their side.''', # Fixed spelling typo "impeccable"
'''**You are the REBEL PUFFERFISH!** 
Traits of this puffer are:
    -passionate
    -impulsive
    -independent
This fugu is the kid your parents told you to watch out for. They march to the beat of their own drum and lead others.
Fiery describes this fish! They have a tough exterior but when they develop bonds, they are unbreakable.
Their only weakness is that they are easily swayed by emotions. If you pull at their heartstrings you will have them eating out of the palm of your hand'''
] # Fixed spelling typo "fiery"

#Each one of the questions are stored in this list
questions_list = [
        '''Question 1: How do you spend your free time?
        a. studying for exams
        b. walking around town
        c. staying at home with a good book
        d. going out with friends
        e. taking care of plants
        f. playing a sport''',
        '''Question 2: Choose an occupation...
        a. archaeologist
        b. real estate agent
        c. marine biologist
        d. university student
        e. CEO of a major company
        f. hair stylist''',
        '''Question 3: Choose one of the following pet companions...
        a. dog
        b. horse
        c. shark
        d. turtle
        e. frog
        f. dolphin''',
        '''Question 4: Favorite form of the potato
        a. baked potatoes
        b. mashed potatoes
        c. french fries
        d. potato chips
        e. potato soup
        f. waffle fries''',
        '''Question 5: What is your ideal home environment?
        a. suburbs
        b. big city
        c. out in the country
        d. in the mountains
        e. near the beach
        f. prison''',
        '''Question 6: What is your beverage of choice?
        a. wine
        b. cola
        c. beer
        d. milk
        e. tea
        f. energy drink''',
        '''Question 7: Someone cuts in front of you at the grocery store, how do you react?
        a. calmly tell them that you were in line (it was probably a mistake)
        b. complain to a worker and make a scene
        c. sternly tell them to go to the back of the line
        d. make a joke out of it, we all make mistakes
        e. let them go ahead of you as if nothing happened
        f. push them out of the line by force, bullying is okay when it's warranted'''
        ,
        '''Question 8: What of the following music genres is your favorite?
        a. classical
        b. jazz
        c. rock
        d. pop
        e. hip-hop
        f. punk''',
        '''Question 9: If you could have any hair color, what would it be?
        a. blue
        b. brown
        c. black
        d. purple
        e. blonde
        f. green''', # I think all natural hair colors should be options. I wanted to choose red :(
        '''Question 10: Which one of these adjectives speaks to you?
        a. valiant
        b. purple
        c. platinum
        d. crazy
        e. golden
        f. free'''
    ]

#The function where the quiz is initialized
def run():
    #Reset all of the personality values at the start of each quiz
    #Each letter represents a personality type
    a_counter = 0
    b_counter = 0
    c_counter = 0
    d_counter = 0
    e_counter = 0
    f_counter = 0
    
    #Introducing the program and collecting a name so that we can put it in the certificate later
    your_name = input("Welcome to the Pufferfish Personality Quiz!\nPlease enter your name: ")

    #Display each individual question and collect the response, then add it to the counter. Repeats this process for every item in the questions list
    for question in questions_list:
        print(question)
        #The while loop is here to catch any invalid inputs so that the question is not skipped
        while True:
            response = input().lower() # This will allow capital and lowercase letters to be accepted
            if response == 'a':
                a_counter += 1
                break
            elif response == 'b':
                b_counter += 1
                break
            elif response == 'c':
                c_counter += 1
                break
            elif response == 'd':
                d_counter += 1
                break
            elif response == 'e':
                e_counter += 1
                break
            elif response == 'f':
                f_counter += 1
                break
            else:
                print("Invalid INPUT")
                continue

    #Puts each of the response counters in a list 
    total_count =  [a_counter, b_counter, c_counter, d_counter, e_counter, f_counter]
    #Using the numpy argmax to find which value in the list is the highest, then returning its index. That index indicates the personality type
    personality = numpy.argmax(total_count)
    #Uses the name given at the start to create a header for the certificate file
    certificate_header = "-----------" + your_name + "'s Pufferfish Personality Quiz Results-----------" # You don't need the backslash for an apostrophe if you use quotation marks around the string
    #Creates a variable 'result' which is a list that includes the header, the corresponding pufferfish ASCII art, and the personality description.
    result =  [certificate_header, str(puffers[int(personality)]), str(puffer_bios[int(personality)])]
    #Joins the elements in 'result' with a newline separating them. This helps the ASCII art to stay intact and keeps the certificate pretty.
    formatted_result = "\n".join(result)
    #Gives us the complete certificate. However, it is not written to any file or printed yet. 
    return formatted_result
    
    
#Opens (and closes) a new file called 'certificate.txt' which is where we will write our certificate file. 
#We do that by simply running the run() function which will return the certificate
with open("certificate.txt", "w") as f:
    f.write(run())

#This is a message telling the user to go to the path where the quiz is saved so that they can find and open up their certificate.
print("THE RESULTS ARE IN! Please check the following directory for 'certificate.txt' --->" + str(path_to_project)) # Again, don't need the backslash for apostrophes
