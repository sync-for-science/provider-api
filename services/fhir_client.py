from fhirclient.client import FHIRClient
from fhirclient.models.fhirsearch import FHIRSearch
from fhirclient.models.location import Location
from fhirclient.models.organization import Organization
from fhirclient.models.practitioner import Practitioner
from fhirclient.models.practitionerrole import PractitionerRole


SETTINGS = {"app_id": "provider_api", "api_base": "http://localhost:8080/baseDstu3"}


CLIENT = FHIRClient(SETTINGS)


def address_to_text(address):
    if address.text:
        return address.text
    lines = address.line[:]
    lines.append("{}, {} {}".format(address.city, address.state, address.postalCode))
    return lines


def practitioner_role_to_output(resource):
    practitioner = resource.practitioner.resolved(Practitioner)
    organization = resource.organization.resolved(Organization)
    location = resource.location[0].resolved(Location)
    return {
        "practitioner_name": practitioner.name[0].text,
        "organization_name": organization.name,
        "address": address_to_text(location.address),
    }


def organization_to_output(resource):
    return {
        "practitioner_name": None,
        "organization_name": resource.name,
        "address": address_to_text(resource.address[0]),
    }


def query_practitioner(args):
    results = query_server(
        PractitionerRole, args, ["location", "practitioner", "organization"]
    )
    return [practitioner_role_to_output(resource) for resource in results]


def query_organization(args):
    results = query_server(Organization, args)
    return [organization_to_output(resource) for resource in results]


def query_server(resource_type, args, includes=None):
    if includes is None:
        includes = list()
    search = FHIRSearch(resource_type, args)
    for include in includes:
        search.include(include)
    return [
        resource
        for resource in search.perform_resources(CLIENT.server)
        if isinstance(resource, resource_type)
    ]
