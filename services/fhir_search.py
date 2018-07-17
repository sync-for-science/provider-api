from services.fhir_client import query_organization, query_practitioner


def search(term):
    results = list()
    results.extend(search_practitioner(term))
    results.extend(search_address(term))
    results.extend(search_organization(term))
    return results


def search_practitioner(term):
    return query_practitioner({"practitioner.name": term})


def search_address(term):
    return query_practitioner({"location.address:contains": term})


def search_organization(term):
    return query_organization({"name:contains": term})
