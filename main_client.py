import rospy
from hsr_agent.agent import Agent


if __name__ == '__main__':
    rospy.init_node('main_client_hsr', disable_signals=True)
    agent = Agent()
    print('TASK')
    print('0 : inspection')
    print('3 : storing_groceries')
    print('4 : serve_breakfast')
    print('6 : clean_the_table')



    task_id = input('task num : ')

    if task_id == '0':
        from task.inspection import inspection
        inspection(agent)
    elif task_id == '3':
        from task.storing_groceries import storing_groceries
        storing_groceries(agent)
    elif task_id == '4':
        from task.serve_breakfast import serve_breakfast
        serve_breakfast(agent)
    elif task_id == '6':
        from task.clean_the_table import clean_the_table
        clean_the_table(agent)
