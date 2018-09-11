import re

print ('welcome to chat-boi say sommethig:\n')


#place holder
def magicParser(sentence):
    return  (sentence)

#place holder
def compose_reply(sentence):
    return sentence

'''
main program
'''
def main():
    looping = True
    while looping:
        user_reply  = input()

        if user_reply == "bye":
            looping = False
                                                   #strip and separate
        user_reply = user_reply.strip() 
                                                          #parse magic
        parsed_reply =  magicParser(user_reply)

                                                      #add ot database
        with open('demo_database.txt','a') as conversation:
            conversation.write('{0}\n'.format(parsed_reply))
        conversation.close()
                                         #give parsed input to chatbot
        bot_reply = compose_reply(parsed_reply)
                                                      # compose answer
        print('CB>> {0}'.format(bot_reply))

       # reloop
main()
