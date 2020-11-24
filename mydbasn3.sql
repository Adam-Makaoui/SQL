--
-- PostgreSQL database dump
--

-- Dumped from database version 10.9 (Ubuntu 10.9-0ubuntu0.18.04.1)
-- Dumped by pg_dump version 10.9 (Ubuntu 10.9-0ubuntu0.18.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: campaign; Type: TABLE; Schema: public; Owner: ishim
--

CREATE TABLE public.campaign (
    cost integer,
    location text,
    duration text,
    id integer NOT NULL
);


ALTER TABLE public.campaign OWNER TO ishim;

--
-- Name: constituents; Type: TABLE; Schema: public; Owner: ishim
--

CREATE TABLE public.constituents (
    constituents_id integer NOT NULL
);


ALTER TABLE public.constituents OWNER TO ishim;

--
-- Name: constituentsemployee; Type: TABLE; Schema: public; Owner: ishim
--

CREATE TABLE public.constituentsemployee (
    wage integer,
    constituents_id integer NOT NULL
);


ALTER TABLE public.constituentsemployee OWNER TO ishim;

--
-- Name: constituentsmisc_supporters; Type: TABLE; Schema: public; Owner: ishim
--

CREATE TABLE public.constituentsmisc_supporters (
    constituents_id integer NOT NULL
);


ALTER TABLE public.constituentsmisc_supporters OWNER TO ishim;

--
-- Name: constituentsvolunteers; Type: TABLE; Schema: public; Owner: ishim
--

CREATE TABLE public.constituentsvolunteers (
    tier integer,
    constituents_id integer NOT NULL
);


ALTER TABLE public.constituentsvolunteers OWNER TO ishim;

--
-- Name: fundedby; Type: TABLE; Schema: public; Owner: ishim
--

CREATE TABLE public.fundedby (
    campaign_id integer NOT NULL,
    funders_id integer NOT NULL
);


ALTER TABLE public.fundedby OWNER TO ishim;

--
-- Name: funders; Type: TABLE; Schema: public; Owner: ishim
--

CREATE TABLE public.funders (
    fund_amount integer,
    funder_id integer NOT NULL
);


ALTER TABLE public.funders OWNER TO ishim;

--
-- Name: fundersfund_rasiers; Type: TABLE; Schema: public; Owner: ishim
--

CREATE TABLE public.fundersfund_rasiers (
    fund_amount integer,
    founders_id integer NOT NULL
);


ALTER TABLE public.fundersfund_rasiers OWNER TO ishim;

--
-- Name: funderslarge_donors; Type: TABLE; Schema: public; Owner: ishim
--

CREATE TABLE public.funderslarge_donors (
    fund_amount integer,
    funders_id integer NOT NULL
);


ALTER TABLE public.funderslarge_donors OWNER TO ishim;

--
-- Name: has; Type: TABLE; Schema: public; Owner: ishim
--

CREATE TABLE public.has (
    campaign_id integer NOT NULL,
    constituentsconstituent_id integer NOT NULL
);


ALTER TABLE public.has OWNER TO ishim;

--
-- Name: question1; Type: VIEW; Schema: public; Owner: ishim
--

CREATE VIEW public.question1 AS
 SELECT campaign.cost,
    campaign.location,
    campaign.duration,
    campaign.id
   FROM public.campaign
  WHERE (campaign.cost < 150);


ALTER TABLE public.question1 OWNER TO ishim;

--
-- Name: question10; Type: VIEW; Schema: public; Owner: ishim
--

CREATE VIEW public.question10 AS
 SELECT constituentsemployee.wage,
    constituentsemployee.constituents_id
   FROM public.constituentsemployee
  WHERE (constituentsemployee.wage > '-1'::integer);


ALTER TABLE public.question10 OWNER TO ishim;

--
-- Name: question2; Type: VIEW; Schema: public; Owner: ishim
--

CREATE VIEW public.question2 AS
 SELECT fundersfund_rasiers.fund_amount,
    fundersfund_rasiers.founders_id
   FROM public.fundersfund_rasiers
  WHERE (EXISTS ( SELECT fundersfund_rasiers_1.fund_amount
           FROM public.fundersfund_rasiers fundersfund_rasiers_1
          WHERE (fundersfund_rasiers_1.fund_amount IS NOT NULL)))
  ORDER BY fundersfund_rasiers.fund_amount DESC;


ALTER TABLE public.question2 OWNER TO ishim;

--
-- Name: question3; Type: VIEW; Schema: public; Owner: ishim
--

CREATE VIEW public.question3 AS
 SELECT campaign.cost,
    campaign.location,
    campaign.duration,
    campaign.id
   FROM public.campaign
  WHERE (campaign.location ~~ '%lon%'::text);


ALTER TABLE public.question3 OWNER TO ishim;

--
-- Name: question4; Type: VIEW; Schema: public; Owner: ishim
--

CREATE VIEW public.question4 AS
 SELECT campaign.cost,
    campaign.location,
    campaign.duration,
    campaign.id
   FROM public.campaign
  WHERE (campaign.duration ~~ '%10%'::text);


ALTER TABLE public.question4 OWNER TO ishim;

--
-- Name: question5; Type: VIEW; Schema: public; Owner: ishim
--

CREATE VIEW public.question5 AS
 SELECT campaign.cost,
    campaign.location,
    campaign.duration,
    campaign.id
   FROM public.campaign
  WHERE (campaign.id IS NOT NULL)
  ORDER BY campaign.cost DESC;


ALTER TABLE public.question5 OWNER TO ishim;

--
-- Name: question6; Type: VIEW; Schema: public; Owner: ishim
--

CREATE VIEW public.question6 AS
 SELECT constituentsvolunteers.tier,
    constituentsvolunteers.constituents_id
   FROM public.constituentsvolunteers
  WHERE (constituentsvolunteers.tier = 1);


ALTER TABLE public.question6 OWNER TO ishim;

--
-- Name: question7; Type: VIEW; Schema: public; Owner: ishim
--

CREATE VIEW public.question7 AS
SELECT
    NULL::integer AS fund_amount,
    NULL::integer AS funders_id;


ALTER TABLE public.question7 OWNER TO ishim;

--
-- Name: question8; Type: VIEW; Schema: public; Owner: ishim
--

CREATE VIEW public.question8 AS
 SELECT campaign.cost,
    campaign.location,
    campaign.duration,
    campaign.id
   FROM public.campaign
  WHERE ((campaign.id >= 1) AND (campaign.id <= 120))
  ORDER BY campaign.id;


ALTER TABLE public.question8 OWNER TO ishim;

--
-- Name: question9; Type: VIEW; Schema: public; Owner: ishim
--

CREATE VIEW public.question9 AS
 SELECT constituentsemployee.wage,
    constituentsemployee.constituents_id
   FROM public.constituentsemployee
  WHERE (constituentsemployee.wage >= 5);


ALTER TABLE public.question9 OWNER TO ishim;

--
-- Data for Name: campaign; Type: TABLE DATA; Schema: public; Owner: ishim
--

COPY public.campaign (cost, location, duration, id) FROM stdin;
100	london	10 days	123
150	victoria	11 days	1234
150	ottawa	12 days	12345
\.


--
-- Data for Name: constituents; Type: TABLE DATA; Schema: public; Owner: ishim
--

COPY public.constituents (constituents_id) FROM stdin;
111
222
333
\.


--
-- Data for Name: constituentsemployee; Type: TABLE DATA; Schema: public; Owner: ishim
--

COPY public.constituentsemployee (wage, constituents_id) FROM stdin;
\N	111
\N	123
\N	321
10	400
5	450
0	455
\.


--
-- Data for Name: constituentsmisc_supporters; Type: TABLE DATA; Schema: public; Owner: ishim
--

COPY public.constituentsmisc_supporters (constituents_id) FROM stdin;
321
222
333
\.


--
-- Data for Name: constituentsvolunteers; Type: TABLE DATA; Schema: public; Owner: ishim
--

COPY public.constituentsvolunteers (tier, constituents_id) FROM stdin;
1	455
1	55
2	155
\.


--
-- Data for Name: fundedby; Type: TABLE DATA; Schema: public; Owner: ishim
--

COPY public.fundedby (campaign_id, funders_id) FROM stdin;
123	100
1234	100
12345	200
123	300
\.


--
-- Data for Name: funders; Type: TABLE DATA; Schema: public; Owner: ishim
--

COPY public.funders (fund_amount, funder_id) FROM stdin;
100	100
500	200
1000	300
\.


--
-- Data for Name: fundersfund_rasiers; Type: TABLE DATA; Schema: public; Owner: ishim
--

COPY public.fundersfund_rasiers (fund_amount, founders_id) FROM stdin;
123	300
234	0
234	60
\.


--
-- Data for Name: funderslarge_donors; Type: TABLE DATA; Schema: public; Owner: ishim
--

COPY public.funderslarge_donors (fund_amount, funders_id) FROM stdin;
234	60
24	70
2	7
\.


--
-- Data for Name: has; Type: TABLE DATA; Schema: public; Owner: ishim
--

COPY public.has (campaign_id, constituentsconstituent_id) FROM stdin;
123	111
1234	222
12345	333
\.


--
-- Name: campaign campaign_pkey; Type: CONSTRAINT; Schema: public; Owner: ishim
--

ALTER TABLE ONLY public.campaign
    ADD CONSTRAINT campaign_pkey PRIMARY KEY (id);


--
-- Name: constituents constituents_pkey; Type: CONSTRAINT; Schema: public; Owner: ishim
--

ALTER TABLE ONLY public.constituents
    ADD CONSTRAINT constituents_pkey PRIMARY KEY (constituents_id);


--
-- Name: constituentsemployee constituentsemployee_pkey; Type: CONSTRAINT; Schema: public; Owner: ishim
--

ALTER TABLE ONLY public.constituentsemployee
    ADD CONSTRAINT constituentsemployee_pkey PRIMARY KEY (constituents_id);


--
-- Name: constituentsmisc_supporters constituentsmisc_supporters_pkey; Type: CONSTRAINT; Schema: public; Owner: ishim
--

ALTER TABLE ONLY public.constituentsmisc_supporters
    ADD CONSTRAINT constituentsmisc_supporters_pkey PRIMARY KEY (constituents_id);


--
-- Name: constituentsvolunteers constituentsvolunteers_pkey; Type: CONSTRAINT; Schema: public; Owner: ishim
--

ALTER TABLE ONLY public.constituentsvolunteers
    ADD CONSTRAINT constituentsvolunteers_pkey PRIMARY KEY (constituents_id);


--
-- Name: fundedby fundedby_pkey; Type: CONSTRAINT; Schema: public; Owner: ishim
--

ALTER TABLE ONLY public.fundedby
    ADD CONSTRAINT fundedby_pkey PRIMARY KEY (campaign_id, funders_id);


--
-- Name: funders funders_pkey; Type: CONSTRAINT; Schema: public; Owner: ishim
--

ALTER TABLE ONLY public.funders
    ADD CONSTRAINT funders_pkey PRIMARY KEY (funder_id);


--
-- Name: fundersfund_rasiers fundersfund_rasiers_pkey; Type: CONSTRAINT; Schema: public; Owner: ishim
--

ALTER TABLE ONLY public.fundersfund_rasiers
    ADD CONSTRAINT fundersfund_rasiers_pkey PRIMARY KEY (founders_id);


--
-- Name: funderslarge_donors funderslarge_donors_pkey; Type: CONSTRAINT; Schema: public; Owner: ishim
--

ALTER TABLE ONLY public.funderslarge_donors
    ADD CONSTRAINT funderslarge_donors_pkey PRIMARY KEY (funders_id);


--
-- Name: has has_pkey; Type: CONSTRAINT; Schema: public; Owner: ishim
--

ALTER TABLE ONLY public.has
    ADD CONSTRAINT has_pkey PRIMARY KEY (campaign_id, constituentsconstituent_id);


--
-- Name: question7 _RETURN; Type: RULE; Schema: public; Owner: ishim
--

CREATE OR REPLACE VIEW public.question7 AS
 SELECT funderslarge_donors.fund_amount,
    funderslarge_donors.funders_id
   FROM public.funderslarge_donors
  WHERE (funderslarge_donors.fund_amount > 0)
  GROUP BY funderslarge_donors.funders_id;


--
-- Name: fundedby fundedby_campaign_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: ishim
--

ALTER TABLE ONLY public.fundedby
    ADD CONSTRAINT fundedby_campaign_id_fkey FOREIGN KEY (campaign_id) REFERENCES public.campaign(id);


--
-- Name: fundedby fundedby_funders_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: ishim
--

ALTER TABLE ONLY public.fundedby
    ADD CONSTRAINT fundedby_funders_id_fkey FOREIGN KEY (funders_id) REFERENCES public.funders(funder_id);


--
-- Name: has has_campaign_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: ishim
--

ALTER TABLE ONLY public.has
    ADD CONSTRAINT has_campaign_id_fkey FOREIGN KEY (campaign_id) REFERENCES public.campaign(id);


--
-- Name: has has_constituentsconstituent_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: ishim
--

ALTER TABLE ONLY public.has
    ADD CONSTRAINT has_constituentsconstituent_id_fkey FOREIGN KEY (constituentsconstituent_id) REFERENCES public.constituents(constituents_id);


--
-- PostgreSQL database dump complete
--

