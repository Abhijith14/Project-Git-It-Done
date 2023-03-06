# Project Git-It-Done


from github import Github
import os


try:
    # Create an action token with your own personal access token
    g = Github(os.environ["ACCESS_TOKEN"])

    user = g.get_user("Abhijith14")

    owner = g.get_user(g.get_user().login)

    # Check if you're already following the user
    auth_user = g.get_user()
    following = False
    for following_user in auth_user.get_following():
        if following_user.login == user.login:
            following = True
            break

    # Follow the user if you're not already following them
    if not following:
        auth_user.add_to_following(user)
        print("You're now following {}.".format(user.login))
    else:
        print("You're already following {}.".format(user.login))

    # Get a list of all repositories owned by the specified owner
    all_repos = user.get_repos()

    # Get a list of all repositories that the owner has starred
    starred_repos = [repo for repo in owner.get_starred()]

    # print(starred_repos)

    # Find all repositories of the user that the owner has starred
    owner_starred_repos = [repo for repo in all_repos for starred_repo in starred_repos if repo.id == starred_repo.id]

    # Find all repositories of the user that the owner has not starred
    owner_not_starred_repos = [repo for repo in all_repos if repo not in starred_repos]

    # Star all repositories of the user that the owner has not starred
    for repo in owner_not_starred_repos:
        auth_user.add_to_starred(repo)
        print(f"Starred repo {repo.full_name}")


    # for repo in owner_starred_repos:
    #     auth_user.remove_from_starred(repo)
    #     print(f"Starred repo {repo.full_name}")
except Exception as e:
    print("Access Failed !!", e)


print("Done!")
