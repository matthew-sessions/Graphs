import random
from collections import deque

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
            return False
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
            return False
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)
            return True

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments
lenth += 1
        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        for i in range(num_users):
            self.add_user(f'User: {i + 1}')

        rand_comb = []
        n = 1
        for i in self.users:
            for a in range(i +1, self.last_id + 1):
                rand_comb.append((i, a))

        random.shuffle(rand_comb)
        # Create friendships

        for i in range(num_users * avg_friendships // 2):
            friendship = rand_comb[i]
            self.add_friendship(friendship[0], friendship[1])
            print(n)
            n += 1

    def populate_graph_linear(self, num_users, avg_friendships):
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME
        for i in range(num_users):
            self.add_user(f'User: {i + 1}')   
        # Add users
        total_friendships = 0
        target_friendships = num_users * avg_friendships // 2
        colis = 0

        while total_friendships < target_friendships:
            user_id = random.randint(1, num_users)     
            freind_id = random.randint(1, num_users)
            if self.add_friendship(user_id, freind_id) == True:
                total_friendships += 1
            else:
                colis += 1

    def get_all_social_paths2(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        q = deque()
        q.append([user_id])
        while q.__len__() > 0:
            path = q.popleft()
            current_id = path[-1]
            if current_id not in visited:
                visited[current_id] = path

                for friend_id in self.friendships[current_id]:
                    path_copy = path.copy()
                    path_copy.append(friend_id)
                    q.append(path_copy)

        
        return visited

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        changin_arr = [user_id]
        depth = 0
        while changin_arr != []:
            new_arr = []
            for i in changin_arr:
                if i not in visited:
                    visited[i] = depth
                    next_friends = self.friendships[i]
                    for a in next_friends:
                        new_arr.append(a)
            depth += 1
            changin_arr = new_arr

        
        return visited

    def socialstats(self, user_id):
        visted = self.get_all_social_paths(user_id)
        visted_arr = [i for i in visted.values()]
        lenth = len(visted_arr)
        avg = sum(visted_arr) / lenth
        
        return lenth, avg

        

if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.socialstats(1)
    print(connections)
