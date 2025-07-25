import os

dirRoot         = os.getcwd()
dirData         = os.path.join(dirRoot,'data')
dirIntermediate = os.path.join(dirRoot,'intermediate')
dirResults      = os.path.join(dirRoot,'results')

# GeoJSON output paths (replacing GDB paths)
strCentersIn  = os.path.join(dirData, r"Wasatch_Choice_Centers_June_2025/WCV_Centers_and_Regional_Land_Uses.shp")
strCentersOut        = os.path.join(dirResults, "Centers.geojson")
strCentersOut_MC     = os.path.join(dirResults, "MetropolitanCenters.geojson")
strCentersOut_UC     = os.path.join(dirResults, "UrbanCenters.geojson")
strCentersOut_CC     = os.path.join(dirResults, "CityCenters.geojson")
strCentersOut_NC     = os.path.join(dirResults, "NeighborhoodCenters.geojson")

strSchoolsIn         = os.path.join(dirData, r"Utah_Schools__from_AGRC_-shp/Schools.dbf")
strSchoolsOut_RegPub = os.path.join(dirResults, "SchoolsRegPublic.geojson")
strSchoolsOut_HighEd = os.path.join(dirResults, "SchoolsHigherEd.geojson")

strATLinesIn  = os.path.join(dirData, r"Active_Transportation_Line_Projects_(2019-2050_RTP)/AT_lines.shp")
strATLinesOut = os.path.join(dirResults, "ActiveTransportationFacilities.geojson")

strTransitIn_Stops   = os.path.join(dirData, r"UTA_Stops_and_Most_Recent_Ridership/UTA_Stops_and_Most_Recent_Ridership.shp")
strTransitIn_830X    = os.path.join(dirData, r"UTA_Stops_and_Most_Recent_Ridership/UTA_Stops_and_Most_Recent_Ridership_830X.shp")
strTransitIn_BRT     = os.path.join(dirData, r"NewTransit/BRT_Stops.shp")
strTransitIn_LRT     = os.path.join(dirData, r"NewTransit/LightRail_Stations.shp")
strTransitIn_CRT     = os.path.join(dirData, r"NewTransit/CommuterRail_Stations.shp")
strTransitOut_Lcl    = os.path.join(dirResults, "LocalBusStops.geojson")
strTransitOut_BrtCur = os.path.join(dirResults, "BRTStops.geojson")
strTransitOut_BrtFut = os.path.join(dirResults, "BRTStops_Future.geojson")
strTransitOut_LrtCur = os.path.join(dirResults, "LRTStops.geojson")
strTransitOut_LrtFut = os.path.join(dirResults, "LRTStops_Future.geojson")
strTransitOut_CrtCur = os.path.join(dirResults, "CRTStops.geojson")
strTransitOut_CrtFut = os.path.join(dirResults, "CRTStops_Future.geojson")

strInterchangesIn_Cur  = os.path.join(dirData, r"Utah_Roads_Freeway_Exits/Roads_FreewayExits.shp")
strInterchangesIn_Fut  = os.path.join(dirData, r"Roadway_Point_Projects_(2019-2050_RTP)/Roadway_points.shp")
strInterchangesOut_Cur = os.path.join(dirResults, "Interchanges.geojson")
strInterchangesOut_Fut = os.path.join(dirResults, "Interchanges_Future.geojson")

strRoadsIn = os.path.join(dirData, r"UtahRoadsNetworkAnalysis/Roads.shp")

strATCycleTracksOut_Cur = os.path.join(dirResults, "ATCycleTracks.geojson")
strATCycleTracksOut_Fut = os.path.join(dirResults, "ATCycleTracks_Future.geojson")

strTrailsAndPathwaysIn = os.path.join(dirData, r"Utah_Trails_and_Pathways/TrailsAndPathways.shp")
strPathsOut_Cur        = os.path.join(dirResults, "ATPaths.geojson")
strPathsOut_Fut        = os.path.join(dirResults, "ATPaths_Future.geojson")

strGroceryIn           = os.path.join(dirData, r"Utah_Grocery_And_Food_Stores__UDAF_-shp/Utah_Grocery_And_Food_Stores__UDAF_.shp")
strHealthCareIn        = os.path.join(dirData, r"Utah_Health_Care_Facilities/HealthCareFacilities.shp")
strParkAccessibilityIn = os.path.join(dirData, r"Park_Accessibility__10_Minute_Walk-shp/WalkAccesstoParks_10Min_Polygons.shp")

strGroceryOut           = os.path.join(dirResults, "GroceryStores.geojson")
strHealthCareOut        = os.path.join(dirResults, "HealthCare.geojson")
strParkAccessibilityOut = os.path.join(dirResults, "ParksAndOpenSpace.geojson")

strChildCareIn  = os.path.join(dirData, r"DayCare/ChildCare.shp")
strChildCareOut = os.path.join(dirResults, "ChildCare.geojson")

strCommunityCenterIn  = os.path.join(dirData, r"Community_Centers/Community_Centers.shp")
strCommunityCenterOut = os.path.join(dirResults, "CommunityCenter.geojson")

strQOZIn  = os.path.join(dirData, r"Utah_Qualified_Opportunity_Zones-shp/UtahQualifiedOpportunityZones.shp")
strQOZOut = os.path.join(dirResults, "UtahQualifiedOpportunityZones.geojson")

strParcelsIn   = os.path.join(dirData, r"remm_base_year_20221003/parcels.shp")
strBuildingsIn = os.path.join(dirData, r"remm_base_year_20221003/buildings.shp")
strParcelsOut  = os.path.join(dirResults, "Parcels.geojson")

strMunicipalitiesIn = os.path.join(dirData, r"Utah_Municipal_Boundaries/Utah_Municipal_Boundaries.shp")
strMetroTownshipsIn = os.path.join(dirData, r"Utah_Metro_Townships/Utah_Metro_Townships.shp")
strCommunitiesOut   = os.path.join(dirResults, "Communities.geojson")

strTAZIn      = os.path.join(dirData, r"USTM_TAZ/TAZ.shp")
strAtoWfrc    = os.path.join(dirData, r"ATO_TDM_Output/ATO19_WFRC.csv")

strTAZwithATOOut = os.path.join(dirResults, "TAZWithATOScores.geojson")
