NEURON {
        ARTIFICIAL_CELL Test
        POINTER ptr     
}

ASSIGNED {
        ptr     
}

INITIAL {
        net_send(1, 1)
}

VERBATIM
extern int (*nrnpy_hoccommand_exec)(Object*);
extern Object** hoc_objgetarg(int);
extern int ifarg(int);
extern void hoc_obj_ref(Object*);
extern void hoc_obj_unref(Object*);
ENDVERBATIM

NET_RECEIVE(w) {
        if (flag == 1) {
VERBATIM
{
	        Object* cb = (Object*)(_p_ptr);
        	if (cb) {
                	(*nrnpy_hoccommand_exec)(cb);
	        }
}
ENDVERBATIM
                net_send(1, 1)
        }
}

PROCEDURE set_callback() {
VERBATIM
        Object** pcb = (Object**)(&(_p_ptr));
	if (*pcb) {
		hoc_obj_unref(*pcb);
		*pcb = (Object*)0;
	}
	if (ifarg(1)) {
		*pcb = *(hoc_objgetarg(1));
		hoc_obj_ref(*pcb);
	}
ENDVERBATIM
}

