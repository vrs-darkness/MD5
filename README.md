# MD5



-> Hashing algorithms are commonly used to convert passwords into hashes which theoretically cannot be deciphered.
But the thing with MD5 is that it has already been certified as an Insecure Hashing Method and we have shifted to much more secure Hashing 
Methods like SH-256 and many more.

-> But Many attempts have been made to make such weak Hashing Algorithm into stronger ones by identifying which compression function would result in Collision.
Collesion here refers to the function being not one-one 
              
                                        f(x1)=f(x2) where x1!=x2
-> This is just one way to crack the Algorithm. There are also few more ways such as Brute Force attack, Rainbow tables which are used to Crack open the algorithms
 firstly Brute force attack tries all the comman passwords available in the database hashes it based on the some specific algo and finally we compare the Hashes!
 Where as Rainbow tables work differently by making up chains of hashes which are also made using the comman password and then optimaly finding where does a 
 desired hash belong to (basically which chain )
 
 -> I aimed at this method (Brute Force + Rainbow Tables)  and tried using Neural Networks for the above Hash Classification. 
    it would be really be beneficial coz we are checking for all the comman passwords ever 
    utilized and also to reduce the time complexity of Brute force. It would be much simpiler to be utilized!!
  
  -> I havn't been able to give promising results but soon i would be performing Hyper-parameter tuning and improvising the model.
    I have attached the research papers that i have utilized for this Repository (https://github.com/vrs-darkness/MD5/tree/main/MD5/Research_Papers)
    I utilized https://github.com/danielmiessler/SecLists/tree/master/Passwords/Common-Credentials this repository to get the comman paswords to make out a dataset out of it!!
    
    
  Happy Learning!!
    
 
                                                 
