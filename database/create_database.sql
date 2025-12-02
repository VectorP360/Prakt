CREATE TABLE public.workshop(
    workshop_id SERIAL PRIMARY KEY,
    name VARCHAR(128) NOT NULL
);

CREATE TABLE public.facility_type(
    facility_type_id SERIAL PRIMARY KEY,
    name VARCHAR(128) NOT NULL
);

CREATE TABLE public.post(
    post_id SERIAL PRIMARY KEY,
    name VARCHAR(128) NOT NULL
);

CREATE TABLE public.facility(
    facility_id SERIAL PRIMARY KEY,
    name VARCHAR(128) NOT NULL,
    
    type_id INTEGER NOT NULL,
    workshop_id INTEGER NOT NULL,
    
    FOREIGN KEY (type_id) REFERENCES public.facility_type (facility_type_id),
    FOREIGN KEY (workshop_id) REFERENCES public.workshop (workshop_id)
);

CREATE TABLE public.scada_scheme(
    scada_scheme_id SERIAL PRIMARY KEY,
    name VARCHAR(128) NOT NULL,
    content TEXT,
    
    facility_id INTEGER NOT NULL,
    FOREIGN KEY (facility_id) REFERENCES public.facility (facility_id)
);

CREATE TABLE public.user(
    user_id SERIAL PRIMARY KEY,
    
    surname VARCHAR(128) NOT NULL,
    name VARCHAR(128) NOT NULL,
    fathersname VARCHAR(128),
    
    hire_date DATE NOT NULL,
    login VARCHAR(128) UNIQUE NOT NULL,
    password VARCHAR(128) NOT NULL,
    
    facility_id INTEGER,
    post_id INTEGER,
    
    FOREIGN KEY (facility_id) REFERENCES public.facility (facility_id),
    FOREIGN KEY (post_id) REFERENCES public.post (post_id)
);

CREATE TABLE public.element_type(
    element_type_id SERIAL PRIMARY KEY,
    name VARCHAR(128) NOT NULL
);

CREATE TABLE public.operation (
    operation_id SERIAL PRIMARY KEY,
    name VARCHAR(128) NOT NULL
);

CREATE TABLE public.element(
    element_id SERIAL PRIMARY KEY,
    name VARCHAR(128) NOT NULL,
    material VARCHAR(128),
    
    element_type_id INTEGER NOT NULL,
    facility_id INTEGER NOT NULL,
    
    FOREIGN KEY (element_type_id) REFERENCES public.element_type (element_type_id),
    FOREIGN KEY (facility_id) REFERENCES public.facility (facility_id)
);

CREATE TABLE public.condition (
    condition_id SERIAL PRIMARY KEY,
    temperature INTEGER,
    loading INTEGER,
    pressure INTEGER,
    facility_id INTEGER NOT NULL,
    
    FOREIGN KEY (facility_id) REFERENCES public.facility (facility_id)
);

CREATE TABLE public.log (
    log_id SERIAL PRIMARY KEY,
    operation_date TIMESTAMP NOT NULL,

    user_id INTEGER,
    operation_id INTEGER,

    FOREIGN KEY (user_id) REFERENCES public.user (user_id),
    FOREIGN KEY (operation_id) REFERENCES public.operation (operation_id)
);