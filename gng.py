#!/usr/bin/env python3

import psycopg2

def main():
    dbconn = psycopg2.connect(host='studsql.csc.uvic.ca', user='ishim', password='a2019river')
    cursor = dbconn.cursor()

    print("\nPlease select a question from q1 - q10 by typing the Question number from the list below \n")
    print("------------Questions to Query from asn3-------------")
    print("1: find all campaigns w/ cost <150")
    print("2: find fundraisers that exist where funds not null and largest funds first")
    print("3: Find all Campaigns in London")
    print("4: find campaign w/ duration 10 days and in victoria")
    print("5: Find campaigns where ID is not null & the largest cost first")
    print("6: Find constituents w/ volunteers where tier = 1")
    print("7: Group donors by their funders ID and find ones that has donated something ")
    print("8: Find campaign IDs b/w 1 and 120 in ascending order")
    print("9: Find all details of wage of employees w/ at least 5 salary")
    print("10: find all employee info that have a non- negative salary")

    print("------------------ OPTIONS / FUNCTIONS------------------")
    print("11: Allows insertion of data into the schema")
    print("12: Displays the inflow and outflow of the schema as a ASCII bar chart")
    print("13: Creative functionality part: 'TABLE DETAILER 2000' views any table + mentions the # of tuples \n")


    # Getting user Input
    choice = int(input("Enter a question number : "))
    
    # CASES
    if choice == 1:
        cursor.execute("""
        select *
        from campaign
        where cost < 150
        """)
        print("Here are the campaigns w/ cost <150\n")
        print("Cost | Location | duration | id ")
        print("-----+----------+----------+---")
        for row in cursor.fetchall():
            print ("%s | %s | %s | %s" % (row[0], row[1], row[2], row[3]))

    if choice == 2:
        cursor.execute("""
        SELECT fundersfund_rasiers.fund_amount,
        fundersfund_rasiers.founders_id
        FROM public.fundersfund_rasiers
        WHERE (EXISTS ( SELECT fundersfund_rasiers_1.fund_amount
        FROM public.fundersfund_rasiers fundersfund_rasiers_1
        WHERE (fundersfund_rasiers_1.fund_amount IS NOT NULL)))
        ORDER BY fundersfund_rasiers.fund_amount DESC;

        """)
        print("Here are the fundrasiers that donated and order with the largest fund_amount\n")
        print("fund_amount | founders_id ")
        print("------------+-------------")

        for row in cursor.fetchall():
            print ("%s | %s" % (row[0], row[1]))

    if choice == 3:
        cursor.execute("""
        SELECT campaign.cost,
        campaign.location,
        campaign.duration,
        campaign.id
        FROM public.campaign
        WHERE (campaign.location ~~ '%lon%'::text);

        """)
        print("Here are the campaigns in London\n")
        print("Cost | Location | duration | id ")
        print("-----+----------+----------+---")
        for row in cursor.fetchall():
            print ("%s | %s | %s | %s" % (row[0], row[1], row[2], row[3]))

    if choice == 4:
        cursor.execute("""
        SELECT campaign.cost,
         campaign.location,
         campaign.duration,
         campaign.id
         FROM public.campaign
         WHERE (campaign.duration ~~ '%10%'::text);

        """)
        print("Here are the campaigns with duration < 10 days and in victoria\n")
        print("Cost | Location | duration | id ")
        print("-----+----------+----------+---")
        for row in cursor.fetchall():
            print ("%s | %s | %s | %s" % (row[0], row[1], row[2], row[3]))

    if choice == 5:
        cursor.execute("""
        SELECT campaign.cost,
        campaign.location,
        campaign.duration,
        campaign.id
        FROM public.campaign
        WHERE (campaign.id IS NOT NULL)
        ORDER BY campaign.cost DESC;

        """)
        print("Here are the campaigns where ID is not null and ordered by the largest\n")
        print("Cost | Location | duration | id ")
        print("-----+----------+----------+---")
        for row in cursor.fetchall():
            print ("%s | %s | %s | %s" % (row[0], row[1], row[2], row[3]))

    if choice == 6:
        cursor.execute("""
        SELECT *
        FROM public.constituentsvolunteers
        WHERE (constituentsvolunteers.tier = 1);

        """)
        print("Here are the Volunteers with tier = 1\n")
        print("tier | constituents_id | annotations")
        print("-----+----------------+-----------")
        for row in cursor.fetchall():
            print ("%s | %s | %s" % (row[0], row[1], row[2]))

    if choice == 7:
        cursor.execute("""
        select *
        from Funders
        Where fund_amount > 0
        group by funders.funder_id

        """)
        print("Here are the campaign IDs b/w 1 & 120 with lowest first\n")
        print("fund_amount | funders_id")
        print("------------+-----------")
        for row in cursor.fetchall():
            print ("%s | %s" % (row[0], row[1]))

    if choice == 8:
        cursor.execute("""
        SELECT campaign.cost,
        campaign.location,
        campaign.duration,
        campaign.id
        FROM public.campaign
        WHERE ((campaign.id >= 1) AND (campaign.id <= 120))
        ORDER BY campaign.id;

        """)
        print("Here are the wages of employees with at least 5 salary\n")
        print("cost | location | duration | id ")
        print("-----+----------+----------+---")
        for row in cursor.fetchall():
            print ("%s | %s | %s | %s" % (row[0], row[1], row[2], row[3]))

    if choice == 9:
        cursor.execute("""
        SELECT *
        FROM public.constituentsemployee
        WHERE (constituentsemployee.wage >= 5);

        """)
        print("Here are the employees w/ a non-negative salary\n")
        print("wage | constituents_id | annotations")
        print("-----+-----------------+------------")
        for row in cursor.fetchall():
            print ("%s | %s | %s" % (row[0], row[1], row[2]))

    if choice == 10:
        cursor.execute("""
        SELECT constituentsemployee.wage,
        constituentsemployee.constituents_id
        FROM public.constituentsemployee
        WHERE (constituentsemployee.wage > '-1'::integer);

        """)
        print("Here are the fundrasiers order with the largest fund_amount\n")
        print("wage | constituents_id ")
        print("-----+-----------------")
        for row in cursor.fetchall():
            print ("%s | %s" % (row[0], row[1]))

    if choice == 11:
        print("---------- Select a TABLE below to insert into ---------\n")


        print("1:  campaigns                   2: constituents             3: constituentsemployee \n"
              "4: constituentsmisc_supporters  5: constituentsvolunteers   6: funders \n"
              "7: fundersfund_rasiers          8: funderslarge_donors ")

        # Getting user Input
        tableChoice = int(input("Enter a table number : "))

        if tableChoice == 1:
            # holding the value to insert
            postgres_insert_query = """ INSERT INTO campaign (cost, location, duration, id) VALUES (%s,%s,%s,%s)"""

            # Getting user data for the entries
            cost = int(input("Enter a cost entry : "))
            location = input("Enter a location record : ")
            duration = input("Enter a duration record : ")
            id = int(input("Enter a id record : "))

            # record to insert by the execute
            record_to_insert = (cost, location, duration, id)

            # actual insertion processes
            cursor.execute(postgres_insert_query, record_to_insert)

            # displaying new table result to user
            print("\nHere is the newly inserted employee table: ")
            cursor.execute(""" select * from campaign """)
            print("Cost | Location | duration | id ")
            print("-----+----------+----------+---")
            for row in cursor.fetchall():
                print ("%s | %s | %s | %s" % (row[0], row[1], row[2], row[3]))

            dbconn.commit()
            count = cursor.rowcount
            print (count, "Record inserted successfully into 'campaign' table")


        if tableChoice == 2:
            # holding the value to insert
            postgres_insert_query = """ INSERT INTO constituents (constituents_id, annotations) VALUES (%s,%s)"""

            # Getting user data for the entries
            constituents_id = int(input("Enter a constituents_id : "))
            annotations = input("Enter an annotation : ")


            # record to insert by the execute
            record_to_insert = (constituents_id, annotations)

            # actual insertion processes
            cursor.execute(postgres_insert_query, record_to_insert)

            #displaying new table result to user
            print("\nHere is the newly inserted employee table: ")
            cursor.execute(""" select * from constituents """)
            print("constituents_id | annotations")
            print("----------------+------------")
            for row in cursor.fetchall():
                print ("%s | %s" % (row[0], row[1]))

            dbconn.commit()
            count = cursor.rowcount
            print ("Record inserted successfully into 'constituents' table at row", count)

        if tableChoice == 3:
            # holding the value to insert
            postgres_insert_query = """ INSERT INTO constituentsemployee (wage, constituents_id, annotations) VALUES (%s,%s,%s)"""

            # Getting user data for the entries
            wage = int(input("Enter a wage  : "))
            constituents_id = int(input("Enter constituents_id  : "))
            annotations = input("Enter an annotation : ")


            # record to insert by the execute
            record_to_insert = (wage, constituents_id, annotations)

            # actual insertion processes
            cursor.execute(postgres_insert_query, record_to_insert)

            #displaying new table result to user
            print("\nHere is the newly inserted constituentsemployee table: ")
            cursor.execute(""" select * from constituentsemployee """)
            print("wage | constituents_id | annotations")
            print("-----+-----------------+------------")
            for row in cursor.fetchall():
                print ("%s | %s | %s" % (row[0], row[1], row[2]))

            dbconn.commit()
            count = cursor.rowcount
            print ("Record inserted successfully into 'constituentsemployee' table at row", count)

        if tableChoice == 4:
            # holding the value to insert
            postgres_insert_query = """ INSERT INTO constituentsmisc_supporters (constituents_id, annotations) VALUES (%s,%s)"""

            # Getting user data for the entries
            constituents_id = int(input("Enter a constituents_id : "))
            annotations = input("Enter an annotation : ")


            # record to insert by the execute
            record_to_insert = (constituents_id,annotations)

            # actual insertion processes
            cursor.execute(postgres_insert_query, record_to_insert)

            #displaying new table result to user
            print("\nHere is the newly inserted constituentsmisc_supporters table: ")
            cursor.execute(""" select * from constituentsmisc_supporters """)
            print("constituents_id | annotations")
            print("---------------+-------------")
            for row in cursor.fetchall():
                print ("%s | %s" % (row[0], row[1]))

            dbconn.commit()
            count = cursor.rowcount
            print ("inserted successfully into 'constituentsmisc_supporters' table at row : ", count)

        if tableChoice == 5:
            # holding the value to insert
            postgres_insert_query = """ INSERT INTO constituentsvolunteers (tier, constituents_id, annotations) VALUES (%s,%s,%s)"""

            # Getting user data for the entries
            tier = int(input("Enter a tier : "))
            constituents_id = int(input("Enter a constituents_id : "))
            annotations = input("Enter an annotation : ")


            # record to insert by the execute
            record_to_insert = (tier, constituents_id, annotations)

            # actual insertion processes
            cursor.execute(postgres_insert_query, record_to_insert)

            #displaying new table result to user
            print("\nHere is the newly inserted employee table: ")
            cursor.execute(""" select * from constituentsvolunteers """)
            print("wage | constituents_id | annotations")
            print("-----+-----------------+------------")
            for row in cursor.fetchall():
                print ("%s | %s | %s" % (row[0], row[1], row[2]))

            dbconn.commit()
            count = cursor.rowcount
            print ("Record inserted successfully into 'constituentsvolunteers' table from row", count)

        if tableChoice == 6:
            # holding the value to insert
            postgres_insert_query = """ INSERT INTO funders (fund_amount, funder_id) VALUES (%s,%s)"""

            # Getting user data for the entries
            fund_amount = int(input("Enter a fund_amount : "))
            funder_id = int(input("Enter a funder_id : "))

            # record to insert by the execute
            record_to_insert = (fund_amount, funder_id)

            # actual insertion processes
            cursor.execute(postgres_insert_query, record_to_insert)

            #displaying new table result to user
            print("\nHere is the newly inserted employee table: ")
            cursor.execute(""" select * from funders """)
            print("fund_amount | funder_id")
            print("------------+----------")
            for row in cursor.fetchall():
                print ("%s | %s" % (row[0], row[1]))

            dbconn.commit()
            count = cursor.rowcount
            print ("Record inserted successfully into 'funders' table at row", count)

        if tableChoice == 7:
            # holding the value to insert
            postgres_insert_query = """ INSERT INTO fundersfund_rasiers (fund_amount, founders_id) VALUES (%s,%s)"""

            # Getting user data for the entries
            fund_amount = int(input("Enter a found_amount : "))
            founders_id = int(input("Enter a founders_id : "))

            # record to insert by the execute
            record_to_insert = (fund_amount, founders_id)

            # actual insertion processes
            cursor.execute(postgres_insert_query, record_to_insert)

            #displaying new table result to user
            print("\nHere is the newly inserted fundersfund_rasiers table: ")
            cursor.execute(""" select * from fundersfund_rasiers """)
            print("fund_amount | founders_id")
            print("------------+------------")
            for row in cursor.fetchall():
                print ("%s | %s" % (row[0], row[1]))

            dbconn.commit()
            count = cursor.rowcount
            print ("Record inserted successfully into 'fundersfund_rasiers' table from row", count)

        if tableChoice == 8:
            # holding the value to insert
            postgres_insert_query = """ INSERT INTO funderslarge_donors (fund_amount, funders_id) VALUES (%s,%s)"""

            # Getting user data for the entries
            fund_amount = int(input("Enter a fund_amount : "))
            founders_id = int(input("Enter a founders_id : "))

            # record to insert by the execute
            record_to_insert = (fund_amount, founders_id)

            # actual insertion processes
            cursor.execute(postgres_insert_query, record_to_insert)

            #displaying new table result to user
            print("\nHere is the newly inserted funderslarge_donors table: ")
            cursor.execute(""" select * from funderslarge_donors """)
            print("fund_amount | founders_id")
            print("------------+------------")
            for row in cursor.fetchall():
                print ("%s | %s" % (row[0], row[1]))

            dbconn.commit()
            count = cursor.rowcount
            print ("Record inserted successfully into 'funderslarge_donors' table from row", count)


    ############### Printing the Chart ################
    if choice == 12:

        print("#-----------------------------------------#")
        #----------------Employee Wage (outflow)---------------
        cursor.execute("""
        SELECT sum(wage)
        FROM constituentsemployee;

        """)

        wageTuple = cursor.fetchone()
        wageSum = int(wageTuple[0])

        print ("Total wage outflow to 'employees' ", wageSum)

        #---------Campaign cost (outflow)----------
        cursor.execute("""
        SELECT sum(cost)
        FROM campaign;

        """)

        costTuple = cursor.fetchone()
        costsum = int(costTuple[0])


        print ("Total Campaign outflow running 'cost' ", costsum)


        #------------Funders fund_amount (inflow)-----------
        cursor.execute("""
        SELECT sum(fund_amount)
        FROM funders;

        """)

        funderTuple = cursor.fetchone()
        fundsum = int(funderTuple[0])

        print ("Total funding/inflow from 'funders' ", fundsum)

        #---------total outflow & inflow-----------

        outflow = wageSum + costsum
        print ("Total outflow : ", outflow)

        inflow = fundsum
        print ("Total inflow : ", inflow)

        #----------------------------------------

        # function to create a Bar Char
        def asciiBarCharOutflow(intNum):
            tempVar = "Outflow: "
            for x in range(0, intNum, 30):
                tempVar += "|";

            print (tempVar)

        # function to create a Bar Char
        def asciiBarCharInflow(intNum):
            tempVar = "Inflow: "
            for x in range(0,intNum,30):
                tempVar+= "|";

            print (tempVar)

        # Calling functions
        asciiBarCharOutflow(outflow)
        asciiBarCharInflow(inflow)
        print("#-----------------------------------------#")


    if choice == 13:
        print("$$$$$$$$ WELCOME TO 'TABLE DETAILER 2000' $$$$$$$$$$$$,\n You can view all data corresponding to a tables/entitys")

        print("Here are the list of tables\n----------------------")

        print("a:  campaign                    b: constituents             c: constituentsemployee \n"
              "d: constituentsmisc_supporters  e: constituentsvolunteers   f: funders \n"
              "g: fundersfund_rasiers          h: funderslarge_donors \n")


        choiceX = input("Enter a table choice between a-h : ")

        # ----------------- campaign -----------------
        if choiceX == "a":
            cursor.execute(""" select * from campaign """)
            print("Here are all the campaigns\n")
            print("Cost | Location | duration | id ")
            print("-----+----------+----------+---")
            for row in cursor.fetchall():
                print ("%s | %s | %s | %s" % (row[0], row[1], row[2], row[3]))
            count = cursor.rowcount
            print ("Total number of tuples in campaign : ", count)


        # ----------------- constituents -----------------
        if choiceX == "b":
            cursor.execute(""" select * from constituents """)
            print("Here are all the constituents\n")
            print("Constituents_id | annotations")
            print("----------------+------------")
            for row in cursor.fetchall():
                print ("%s | %s" % (row[0], row[1]))
            count = cursor.rowcount
            print ("Total number of tuples in constituents : ", count)

        # ----------------- constituentsemployee -----------------
        if choiceX == "c":
            cursor.execute(""" select * from constituentsemployee """)
            print("Here are all the constituentsemployee\n")
            print("Wage | Constituents_id | annotations ")
            print("-----+----------+----------+---")
            for row in cursor.fetchall():
                print ("%s | %s | %s" % (row[0], row[1], row[2]))
            count = cursor.rowcount
            print ("Total number of tuples in campaign : ", count)

        # ----------------- constituentsmisc_supporters -----------------
        if choiceX == "d":
            cursor.execute(""" select * from constituentsmisc_supporters """)
            print("Here are all the constituentsmisc_supporters\n")
            print("Constituents_id | annotations")
            print("----------------+------------")
            for row in cursor.fetchall():
                print ("%s | %s" % (row[0], row[1]))
            count = cursor.rowcount
            print ("Total number of tuples in constituentsmisc_supporters : ", count)

        # ----------------- constituentsvolunteers -----------------
        if choiceX == "e":
            cursor.execute(""" select * from constituentsvolunteers """)
            print("tier | Constituents_id | annotations ")
            print("-----+----------+----------+---")
            for row in cursor.fetchall():
                print ("%s | %s | %s" % (row[0], row[1], row[2]))
            count = cursor.rowcount
            print ("Total number of tuples in constituentsvolunteers : ", count)

        # ----------------- funders -----------------
        if choiceX == "f":
            cursor.execute(""" select * from funders """)
            print("Here are all the funders\n")
            print("fund_amount | funder_id")
            print("------------+----------")
            for row in cursor.fetchall():
                print ("%s | %s" % (row[0], row[1]))
            count = cursor.rowcount
            print ("Total number of tuples in funders : ", count)

        # ----------------- fundersfund_rasiers -----------------
        if choiceX == "g":
            cursor.execute(""" select * from fundersfund_rasiers """)
            print("Here are all the fundersfund_rasiers\n")
            print("fund_amount | funder_id")
            print("------------+----------")
            for row in cursor.fetchall():
                print ("%s | %s" % (row[0], row[1]))
            count = cursor.rowcount
            print ("Total number of tuples in fundersfund_rasiers : ", count)


        # ----------------- funderslarge_donors -----------------
        if choiceX == "h":
            cursor.execute(""" select * from funderslarge_donors """)
            print("Here are all the funderslarge_donors\n")
            print("fund_amount | funder_id")
            print("------------+----------")
            for row in cursor.fetchall():
                print ("%s | %s" % (row[0], row[1]))
            count = cursor.rowcount
            print ("Total number of tuples in funderslarge_donors : ", count)

    # ending playing w/ db
    cursor.close()
    dbconn.close()



if __name__ == "__main__": main()
