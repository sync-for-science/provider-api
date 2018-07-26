from services.fhir_client import query_organization, query_practitioner


def key(term):
    return term.get("practitioner_name") or term.get("organization_name")


def search(term):
    results = list()
    results.extend(search_practitioner(term))
    results.extend(search_address(term))
    results.extend(search_organization(term))
    return sorted(results, key=key)


def search_practitioner(term):
    return query_practitioner({"practitioner.name": term})


def search_address(term):
    practitioners = query_practitioner({"location.address:contains": term})
    organizations = query_organization({"address:contains": term})
    return practitioners + organizations


def search_organization(term):
    return query_organization({"name:contains": term})
