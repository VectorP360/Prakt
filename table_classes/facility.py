import table_classes.facility_types as facility_types
import table_classes.workshop as workshop
import table_classes.scada_scheme as scada_scheme

class Facility:
    def __init__(self, facility_ID:int, type: facility_types.FacilityTypes, workshop: workshop.Workshop, scada_schema: scada_scheme.SCADA_scheme):
        self.facility_ID = facility_ID
        self.type = type
        self.workshop = workshop
        self.scada_schema = scada_schema