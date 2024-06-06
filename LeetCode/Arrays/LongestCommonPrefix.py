
# def longestCommonPrefix(strs ):
#         word = strs[0]
#         for i in range(1,len(strs)-1):
#             for i in range(0,len(word)-1):
#                 if word[i] != strs[i][i]:
#                     word = word[:i] # slice the word from the beginning to the index of the mismatch
#                     break


#         return word


            



# strs = ["f;ower","f;ow","f;ght"]
# print(longestCommonPrefix(strs))












# #include <pthread.h>
# #include <stdio.h>
# #include <stdlib.h>

# void *func(void *arg) {
#   pthread_detach(pthread_self());
#   printf("Inside the thread\n");
#   pthread_exit(NULL);
# }

# int main() {
#   pthread_t ptid;

#   pthread_create(&ptid, NULL, &func, NULL);

#   printf("This line may be printed before thread terminates\n");

#   // Thread comparison is included for demonstration purposes, 
#   // typically not required in most scenarios.
#   if (pthread_equal(ptid, pthread_self())) {
#     printf("Threads are equal\n");
#   } else {
#     printf("Threads are not equal\n");
#   }

#   pthread_join(ptid, NULL);

#   printf("This line will be printed after thread ends\n");
  
#   pthread_exit(NULL);
# }














class Solution:
    def isValid(self, s: str) -> bool:
         stack = ''
         for i in range(0,len(s)-1):
            if(s[i] == '(' or s[i] == '{' or s[i] == '['):
                stack.append(s[i])
            if(s[i] == ')' or s[i] == '}' or s[i] == ']'):
                char = stack.pop()
                if{}


