//
// Created by mac on 1/7/23.
//


#include<stdio.h>
#include<stdbool.h>
#include<stdlib.h>
#include<string.h>


typedef struct {
    int k;
    int value;
    int head;
    int size;
    int rubbish;
    int *arr;
} DataStream;


DataStream *dataStreamCreate(int value, int k) {
    DataStream *new = (DataStream *) malloc(sizeof(DataStream));
    new->arr = (int *) calloc(1e5 + 1, sizeof(int));
    new->size = 0;
    new->head = 0;
    new->k = k;
    new->value = value;
    new->rubbish = 0;
    return new;
}

bool dataStreamConsec(DataStream *obj, int num) {
    if (obj->size < obj->k - 1) {
        obj->arr[obj->size++] = num;
        if (num != obj->value) obj->rubbish++;
        return false;
    } else if (obj->size == obj->k - 1) {
        // First come
        obj->arr[obj->size++] = num;
        if (num != obj->value) obj->rubbish++;
        if (obj->rubbish == 0) return true;
        else return false;
    } else {
        if (obj->arr[obj->head] != obj->value)
            obj->rubbish--;
        obj->head++;
        obj->arr[obj->size++] = num;
        if (num != obj->value) {
            obj->rubbish++;
            return false;
        } else {
            if (obj->rubbish == 0)
                return true;
            else
                return false;
        }
    }
}

void dataStreamFree(DataStream *obj) {
    free(obj->arr);
}

/**
 * Your DataStream struct will be instantiated and called as such:
 * DataStream* obj = dataStreamCreate(value, k);
 * bool param_1 = dataStreamConsec(obj, num);

 * dataStreamFree(obj);
*/
int main(void) {
    printf("Hello World\n");
    return 0;
}
