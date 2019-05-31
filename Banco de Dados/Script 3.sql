if DB_ID('DBWIKI') is null
	create database DBWIKI;
go

USE DBWIKI

if OBJECT_ID('WIKI_RECENT_CHANGE') IS NULL
begin
	CREATE TABLE WIKI_RECENT_CHANGE (
	id int identity,
	rc_Date        DATETIME				NOT NULL,    
	rc_user        varchar(40)  		NOT NULL    DEFAULT 0,    		
	rc_namespace   int		            NOT NULL    DEFAULT 0,    
	rc_title       varchar(255)         ,    	
	rc_server_name varchar(100)         )

	ALTER TABLE WIKI_RECENT_CHANGE
		ADD CONSTRAINT PK_WIKI_RECENT_CHANGE PRIMARY KEY (id);
END
ELSE 
  TRUNCATE TABLE WIKI_RECENT_CHANGE
go


CREATE OR ALTER PROCEDURE [dbo].[SP_INSERT_RC] 

 @rc_Date DATETIME       = NULL
,@rc_user varchar(255)        = NULL
,@rc_namespace int             = NULL
,@rc_title varchar(255)      = NULL
,@rc_server_name varchar(100) = null

AS
	INSERT INTO [dbo].[WIKI_RECENT_CHANGE]
           ([rc_Date]
           ,[rc_user]
           ,[rc_namespace]
           ,[rc_title]           
		   ,[rc_server_name])
     VALUES
           (   @rc_Date             
           	  ,@rc_user     
              ,@rc_namespace
              ,@rc_title    			  
			  ,@rc_server_name)
