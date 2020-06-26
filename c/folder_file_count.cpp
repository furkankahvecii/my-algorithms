#include <stdio.h>
#include <stdlib.h>
#include <io.h>
#include <sys/stat.h>
#include <dirent.h> 

void traverseDirectory(char path[100]){
    DIR* dir;
    struct dirent *ent;
    struct stat s;
	
	int folder_count = 0, file_count = 0;
			
    dir = opendir(path);
	
    while((ent=readdir(dir)) != NULL){
    	
    	char * each_path = strstr(ent->d_name, ".");
    	if(each_path != NULL && ent->d_name[0] == each_path[0] == '.'){
    		continue;
		}
    	if(!strcmp(".", ent->d_name) || !strcmp("..", ent->d_name)){
            continue;
        }
        else{
        	            	
        	char localname[100];
			strcpy(localname, path);
			strcat(localname,"\\");
			strcat(localname,ent->d_name);

			if( stat(localname,&s) == 0 )
			{
			    if( s.st_mode & S_IFDIR )
			    {
					folder_count++;
			    }
			    else if( s.st_mode & S_IFREG )
			    {
			    	file_count++;
			    }
			    else
			    {
			        continue;
			    }
			}
			else
			{
			    continue;
			}
		}  
    }
    
    closedir(dir);
    printf("Folder count = %d \nFile Count = %d",folder_count,file_count);
}

void main()
{
	char path[100] = "yourpath"; // C:\\Users\\UsersX\\Desktop\\folder1
	traverseDirectory(path);
}

