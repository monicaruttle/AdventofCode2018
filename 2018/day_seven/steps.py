from Rule import Rule
from Worker import Worker

def build_dependency_tree(requirements, dependencies):
    with open('DaySeven.txt') as instruction_file:
        instructions = instruction_file.readlines()
    
    for instruction in instructions:
        rule = Rule(instruction)

        if rule.second not in requirements:
            requirements[rule.second] = []
        if rule.first not in dependencies:
            dependencies[rule.first] = []

        requirements[rule.second].append(rule.first)
        dependencies[rule.first].append(rule.second)

    return 

def determine_path():
    requirements = {} # Step mapping to a list of steps it requires
    dependencies = {} # Step mapping which steps can come after
    build_dependency_tree(requirements, dependencies)

    # determine first step
    all_steps = set(requirements.keys() + dependencies.keys())

    completed_steps = []
    possible_steps = [x for x in all_steps if x not in requirements]
    while len(completed_steps) < len(all_steps):
        next_step = min(possible_steps)
        possible_steps.remove(next_step)

        completed_steps.append(next_step)

        for dependency in dependencies.get(next_step, []):
            if all(requirement in completed_steps for requirement in requirements[dependency]) and dependency not in possible_steps:
                possible_steps.append(dependency)
    
    print(''.join(completed_steps))

def determine_path_multiple_workers():
    requirements = {} # Step mapping to a list of steps it requires
    dependencies = {} # Step mapping which steps can come after
    build_dependency_tree(requirements, dependencies)

    # determine first step
    all_steps = set(requirements.keys() + dependencies.keys())

    completed_steps = []
    possible_steps = [x for x in all_steps if x not in requirements]
    workers = [Worker(i) for i in range(1, 5)]
    
    current_second = 0
    while len(completed_steps) < len(all_steps):
        # determine the next work to start
        for worker in workers:
            if not worker.is_free():
                continue
            if len(possible_steps) > 0:
                next_step = min(possible_steps)
                possible_steps.remove(next_step)

                worker.start_progress(next_step)

        # determine if any workers are done
        for worker in workers:
            completed_step = worker.countdown()
            if completed_step is not None:
                print('Completing step: {}'.format(completed_step))
                completed_steps.append(completed_step)

            for dependency in dependencies.get(completed_step, []):
                if all(requirement in completed_steps for requirement in requirements[dependency]) and dependency not in possible_steps:
                    possible_steps.append(dependency)

        current_second += 1
    print(current_second)



if __name__ == '__main__':
    determine_path_multiple_workers()
