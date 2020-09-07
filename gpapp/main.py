#coding:utf-8
#!/usr/bin/env python

import inspect
# ~ from chat import Chat
from question import UserQuestion
from answer import GpAnswer


#=======================
# main script execution
#=======================
def main():
    """
        request limitation to 10
        from the user after politeness check
        and without coarseness
    """
    #---------------------------------
    # awaits the courtesy of the user
    #---------------------------------
    grandpy = GpAnswer()
    user = UserQuestion()
    comprehension = ""
    # grandpy presentation archiving
    accueil = f"Accueil de {grandpy.grandpy}"\
        +" ==> Bonjour Mon petit, en quoi puis-je t'aider ?"
    print(f"\n{accueil}")
    print(grandpy.name("main"))
    print(grandpy.nb_line(inspect.currentframe().f_lineno+2), end=" ==> ")
    print(grandpy.call("add_message", "QuestionParameter"))
    grandpy.add_message(accueil, grandpy.grandpy)
    # waiting for user question
    print(grandpy.name("main"))
    print(grandpy.nb_line(inspect.currentframe().f_lineno+2), end=" ==> ")
    print(grandpy.call("response_user", type(user).__name__))
    user.response_user()
    # udetermines the comprehension value in the user question
    print(grandpy.name("main"))
    print(grandpy.nb_line(inspect.currentframe().f_lineno+2), end=" ==> ")
    print(grandpy.call("user_comprehension", type(user).__name__))
    user.user_comprehension()
    comprehension = grandpy.comprehension
    # back after the first analysis
    print(grandpy.name("main"))
    print(grandpy.nb_line(inspect.currentframe().f_lineno+2), end=" ==> ")
    print(grandpy.return_line(),"\n")
    # analyze the value of understanding
    print(comprehension)
    if not comprehension:
        while grandpy.nb_incomprehension < 3 and not comprehension:
            grandpy.nb_incomprehension += 1
            #           -------------------
            print(inspect.currentframe().f_lineno+3, end=" ==> ")
            print(grandpy.call("Appel","response_user", type(user).__name__),"\n")
            #           -------------------
            user.response_user(question)
            user.user_comprehension()

    else:
        print("je suis ici")

    # ~ while grandpy.nb_incivility < 3\
        # ~ and grandpy.nb_incomprehension < 3\
        # ~ and grandpy.nb_indecency< 3:

        # Test decency
        # ~ print(f"\n{inspect.currentframe().f_lineno + 2}", end=".")
        # ~ print(f" Appel de {user.user_decency.__name__}")
        # ~ user.user_decency()

        # ~ if not user.decency\
            # ~ and user.decency != user.comprehension\
            # ~ and user.civility != user.comprehension:

            # ~ dialog.nb_indecency += 1
        # ~ print(f"\nligne {inspect.currentframe().f_lineno} nombre indecency", end=" = ")
        # ~ print(f"{dialog.nb_indecency}")

        # ~ # Test civility
        # ~ print(f"\n{inspect.currentframe().f_lineno + 2}", end=".")
        # ~ print(f" Appel de {user.user_civility.__name__}")
        # ~ user.user_civility()
        # ~ if not user.civility and (user.decency and user.civility) != user.comprehension:
            # ~ dialog.nb_incivility += 1
        # ~ print(f"\nligne {inspect.currentframe().f_lineno} ==> {dialog.nb_incivility}")

        # ~ # Test comprehension
        # ~ print(f"\n{inspect.currentframe().f_lineno + 2}", end=".")
        # ~ print(f" Appel de {user.user_comprehension.__name__}\n")
        # ~ user.user_comprehension()
        # ~ if not user.comprehension:
            # ~ dialog.nb_incomprehension += 1
        # ~ else:
            # ~ user.comprehension = False
        # ~ print(
            # ~ f"ligne {inspect.currentframe().f_lineno} ==> {dialog.nb_incomprehension}"
        # ~ )
        # ~ dialog.display_status()
        # ~ # unrecognized / recognized words
        # ~ if user.comprehension:
            # ~ print(f"\nje passe par la ligne {inspect.currentframe().f_lineno}")
            # ~ dialog.display_status()
            # ~ # rudeness of the user
            # ~ if not user.decency:
                # ~ print(f"\nje passe par la ligne {inspect.currentframe().f_lineno}")
                # ~ user.rude_user()
                # ~ # rudeness of the user
                # ~ if not user.civility:
                    # ~ print(f"\nje passe par la ligne {inspect.currentframe().f_lineno}\n")
                    # ~ print(f"{inspect.currentframe().f_lineno + 2}", end=".")
                    # ~ print(f" Appel de {user.unpoliteness_user.__name__}")
                    # ~ user.unpoliteness_user()
                    # ~ print(f"la ligne {inspect.currentframe().f_lineno}")
                # ~ else:
                    # ~ print(f"\nje passe par la ligne {inspect.currentframe().f_lineno}")

            # ~ else:
                # ~ print(f"\nje passe par la ligne {inspect.currentframe().f_lineno}\n")
                # ~ print(f"{inspect.currentframe().f_lineno + 2}", end=".")
                # ~ print(f" Appel de {dialog.rude_user.__name__}")
                # ~ user.rude_user()
                # ~ print(f"la ligne {inspect.currentframe().f_lineno}")
        # ~ else:
            # ~ print(f"\nje passe par la ligne {inspect.currentframe().f_lineno}\n")
            # ~ print(f"\n{inspect.currentframe().f_lineno + 2}", end=".")
            # ~ print(f" Appel de {grandpy.question_incorrect.__name__}")
            # ~ grandpy.question_incorrect()
            # ~ print(f"la ligne {inspect.currentframe().f_lineno}")
            # ~ dialog.display_status()
            # ~ print(f"\nje passe par la ligne {inspect.currentframe().f_lineno}\n")
        # ~ if dialog.nb_incivility >= 3:
            # ~ dialog.quotas = True
            # ~ print(
                # ~ f"{inspect.currentframe().f_lineno}. Cette IMPOLITESSE me FATIGUE ... !"
            # ~ )
            # ~ user.reconnection()
            # ~ print(f"la ligne {inspect.currentframe().f_lineno}")
        # ~ elif dialog.nb_indecency >= 3:
            # ~ dialog.quotas = True
            # ~ print(f"\n{inspect.currentframe().f_lineno + 2}", end=".")
            # ~ print(f" Appel de {grandpy.stress_decency.__name__}")
            # ~ grandpy.stress_decency()
            # ~ print(f"la ligne {inspect.currentframe().f_lineno}")
        # ~ elif dialog.nb_incomprehension >= 3:
            # ~ dialog.quotas = True
            # ~ print(
                # ~ f"{inspect.currentframe().f_lineno}. Aujourd'hui je ne suis pas au TOP ... !"
            # ~ )
            # ~ grandpy.reconnection()
            # ~ print(f"la ligne {inspect.currentframe().f_lineno}")
        # ~ else:
            # ~ # Waits for user new question
            # ~ print("question")
            # ~ dialog.nb_request = 0
            # ~ while not dialog.quotas:
                # ~ # maximum number of responses reached
                # ~ if dialog.nb_request >= 10:
                    # ~ dialog.quotas = True

                # ~ # Grandpy starts to tire
                # ~ if dialog.nb_request == 5:

                    # ~ response = "Houla ma mémoire n'est plus ce qu'elle était ... "
                    # ~ print(response)
                    # ~ dialog.add_message(response, dialog.grandpy)

                # ~ # grandpy's reply
                # ~ print()
                # ~ print(f"{inspect.currentframe().f_lineno + 2}", end=".")
                # ~ print(f" Appel de {dialog.waiting_question.__name__}")
                # ~ dialog.waiting_question()

                # ~ # decency in response
                # ~ if dialog.decency:
                    # ~ while dialog.decency and dialog.nb_indecency < 3:
                        # ~ dialog.nb_indecency += 1
                        # ~ dialog.decency = False
                        # ~ print()
                        # ~ print(f"{inspect.currentframe().f_lineno + 2}", end=".")
                        # ~ print(f" Appel de {dialog.rude_user.__name__}")
                        # ~ dialog.rude_user()

                        # ~ if not dialog.decency:
                            # ~ dialog.nb_request -= 1
                            # ~ if dialog.nb_request < 0:
                                # ~ dialog.nb_request = 0


                        # ~ # big stress of Grandpy because of decency ==> back in 24 hours
                        # ~ if dialog.nb_indecency >= 3:
                            # ~ dialog.quotas = True
                            # ~ print(f"\n{inspect.currentframe().f_lineno + 2}", end=".")
                            # ~ print(f" Appel de {grandpy.stress_decency.__name__}")
                            # ~ grandpy.stress_decency()
                # ~ else:
                    # ~ print()
                    # ~ print(f"{inspect.currentframe().f_lineno + 2}", end=".")
                    # ~ print(f" Appel de {dialog.answer_returned.__name__}")
                    # ~ dialog.answer_returned()

            # ~ if dialog.nb_request >= 10 and dialog.nb_indecency < 3:
                # ~ # grandpy exhaustion
                # ~ response = "cette séance de recherche me FATIGUE ..."
                # ~ print(response)
                # ~ dialog.add_message(response, dialog.grandpy)
                # ~ print()
                # ~ print(f"{inspect.currentframe().f_lineno + 2}", end=".")
                # ~ print(f" Appel de {dialog.reconnection.__name__}")
                # ~ dialog.reconnection()

        # ~ # display chat setting status
        # ~ print(f"{inspect.currentframe().f_lineno + 2}", end=".")
        # ~ print(f" Appel de {dialog.display_status.__name__}\n")
        # ~ dialog.display_status()

            # ~ # display chat setting status
            # ~ print(f"{inspect.currentframe().f_lineno + 2}", end=".")
            # ~ print(f" Appel de {dialog.display_status.__name__}\n")
            # ~ dialog.display_status()

            # ~ dialog.nb_request += 1

        # ~ print(f"{inspect.currentframe().f_lineno + 2}", end=".")
        # ~ print(f" Appel de {dialog.user_decency.__name__}\n")
        # ~ dialog.user_civility()

        # ~ print(f"j'arrive sur la ligne {inspect.currentframe().f_lineno}\n")
        # ~ print(f"{inspect.currentframe().f_lineno + 2}", end=".")
        # ~ print(f" Appel de {dialog.display_status.__name__}")
        # ~ dialog.display_status()
        # ~ print(f"retour sur la ligne {inspect.currentframe().f_lineno}")

    # ~ # too many unrecognized words
    # ~ if not user.comprehension:
        # ~ dialog.quotas = True
        # ~ response = "Je n'arrive a trouver une réponse !"
        # ~ print(response)
        # ~ dialog.add_message(response, dialog.grandpy)
        # ~ print()
        # ~ print(f"{inspect.currentframe().f_lineno + 2}", end=".")
        # ~ print(f" Appel de {dialog.reconnection.__name__}")
        # ~ dialog.reconnection()
    # ~ print()
    # ~ dialog.nb_request = 0
    # ~ print(f"{inspect.currentframe().f_lineno + 2}", end=".")
    # ~ print(f" Appel de {dialog.user_civility.__name__}")
    # ~ dialog.user_civility()

    # ~ # rudeness of the user
    # ~ if not user.civility and user.comprehension:
        # ~ dialog.display_status()
        # ~ while not user.civility and dialog.nb_request < 3:
            # ~ print(f"je passe par la ligne {inspect.currentframe().f_lineno}\n")
            # ~ print(f"{inspect.currentframe().f_lineno + 2}", end=".")
            # ~ print(f" Appel de {dialog.user_comprehension.__name__}\n")
            # ~ dialog.unpoliteness_user()
            # ~ print(f"\n{inspect.currentframe().f_lineno + 2}", end=".")
            # ~ print(f" Appel de {dialog.user_comprehension.__name__}")
            # ~ dialog.user_comprehension()

            # ~ if user.civility:
                # ~ dialog.nb_request -= 1
                # ~ if dialog.nb_request < 0:
                    # ~ dialog.nb_request = 0

            # ~ dialog.nb_request += 1

            # ~ if not user.comprehension:
                # ~ while not comprehension:
                    # ~ user.comprehension = True
                    # ~ print(f"je passe par la ligne {inspect.currentframe().f_lineno}\n")
                    # ~ print(f"{inspect.currentframe().f_lineno + 2}", end=".")
                    # ~ print(f" Appel de {dialog.user_comprehension.__name__}\n")
                    # ~ dialog.unpoliteness_user()

        # ~ # big stress of Grandpy because of incivility ==> back in 24 hours
        # ~ if dialog.nb_request >= 3:
            # ~ response = "cette impolitesse me FATIGUE ..."
            # ~ print(response)
            # ~ dialog.quotas = True
            # ~ dialog.add_message(response, dialog.grandpy)
            # ~ print()
            # ~ print(f"{inspect.currentframe().f_lineno}", end=".")
            # ~ print(f" Appel de {dialog.reconnection.__name__}")
            # ~ dialog.reconnection()


    # ~

if __name__ == "__main__":
    main()
