class Solution:
    def findAllRecipes(self, recipes: list[str], ingredients: list[list[str]], supplies: list[str]) -> list[str]:
        n: int = len(recipes)
        supplies = set(supplies)
        res = set()
        created = set()

        flag = True
        while flag:
            flag = False
            for ind in range(n):
                if ind not in created:
                    can_create = True
                    for ingredient in ingredients[ind]:
                        if not ingredient in supplies and not ingredient in res:
                            can_create = False
                            break
                    if can_create:
                        res.add(recipes[ind])
                        created.add(ind)
                        flag = True

        return list(res)


# O(n^2), will return later to make topo sort solution
