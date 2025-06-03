import repository_classes

workshop_repo = repository_classes.WorkshopRepository(1)
workshop_repo.create()
workshop_repo.workshop_id = 2
workshop_repo.create()
print(workshop_repo.read(1).__dict__)
print(workshop_repo.read(2).__dict__)
workshop_repo.update(2,3)
print(workshop_repo.read(3).__dict__)