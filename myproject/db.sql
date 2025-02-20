CREATE TABLE 'Class' (
    'class_id'    int(11)    NOT NULL,
    'class_name'    varchar(30)    NOT NULL,
    'class_loc'    varchar(30)    NOT NULL,
    'class_article'    varchar(100)    NOT NULL,
    'teacher'    varchar(10)    NOT NULL,
    'teacher_article'    varchar(100)    NOT NULL,
    'max_people'    int(11)    DEFAULT 0,
    'now_people'    int(11)    DEFAULT 0,
    'price'    int(11)    DEFAULT 0,
    'is_closed'    bool    DEFAULT 0,
    PRIMARY KEY ('class_id')   
);