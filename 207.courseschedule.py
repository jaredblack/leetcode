from collections import defaultdict

# this is just straight up the neetcode solution
# I understand it now but it would be a good one to revisit
def canFinish(numCourses: int, prerequisites: list[list[int]]) -> bool:
    pre_dict = defaultdict(list)
    for course, prereq in prerequisites:
        pre_dict[course].append(prereq)

    visit_set = set()
    def dfs(course):
        if course in visit_set:
            return False
        if pre_dict[course] == []:
            return True
        
        visit_set.add(course)
        for pre in pre_dict[course]:
            if not dfs(pre): return False
        visit_set.remove(course)
        pre_dict[course] = []
        return True

    for i in range(numCourses):
        if not dfs(i): return False
    return True